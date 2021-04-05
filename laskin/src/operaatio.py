class Operaatio:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.logiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def _kasittele_syote(self):
        arvo = 0

        try:
            arvo = int(self.lue_syote())
        except Exception:
            print('ei onnistu', self.lue_syote)
            pass

        return arvo

    def _kumoa(self):
        self.logiikka.aseta_arvo(self.logiikka.get_edellinen())
