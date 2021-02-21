import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
    
class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.asiakas = 'mikko'
        self.asiakas_tilinumero = '12345'

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, 'maito', 5)
            if tuote_id == 2:
                return Tuote(2, 'piima', 6)
            if tuote_id == 3:
                return Tuote(3, 'macbook pro', 8357899)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()
    
    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called()

    def test_tilisiirtoa_kutsutuaan_oikeilla_parametreilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, self.viitegeneraattori_mock.uusi(), self.asiakas_tilinumero, self.kauppa.get_tilinumero(), 5
        )

    def test_oikea_tilisiirto_kahdella_eri_tuotteella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, self.viitegeneraattori_mock.uusi(), self.asiakas_tilinumero, self.kauppa.get_tilinumero(), 11
        )

    def test_oikea_tilisiirto_kahdella_samalla_tuotteella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, self.viitegeneraattori_mock.uusi(), self.asiakas_tilinumero, self.kauppa.get_tilinumero(), 10
        )

    def test_puuttuvaa_tuotetta_ei_veloiteta(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)

        self.pankki_mock.tilisiirto.assert_called_with(
            self.asiakas, self.viitegeneraattori_mock.uusi(), self.asiakas_tilinumero, self.kauppa.get_tilinumero(), 5
        )

    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 0)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 0)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi()
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 0)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.asiakas, self.asiakas_tilinumero)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_korista_poistaminen_onnistuu(self):
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 0)
        self.kauppa.lisaa_koriin(1)
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 5)
        self.kauppa.poista_korista(1)
        self.assertEqual(self.kauppa.get_ostoskori().hinta(), 0)
        