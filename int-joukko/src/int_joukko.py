KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [None] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.lukujono

    def luo_laajempi_taulukko(self):
        taulukko_old = self.lukujono
        self.lukujono = [None] * (self.alkioiden_lkm + self.kasvatuskoko)
        
        for i in range(0, len(taulukko_old)):
            self.lukujono[i] = taulukko_old[i]

    def lisaa(self, luku):

        if self.kuuluu(luku):
            return False

        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.lukujono) == 0:
            self.luo_laajempi_taulukko()

        return True

    def etsi_luku(self, luku):
        pass

    def poista(self, luku):

        if not self.kuuluu(luku):
            return False

        self.lukujono.remove(luku)
        self.alkioiden_lkm -= 1
        return True


    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.lukujono if luku]

    @staticmethod
    def _alusta_joukko_operaatio(a, b):
        joukko=IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        return (joukko, a_taulu, b_taulu)

    @staticmethod
    def yhdiste(a, b):
        x, a_taulu, b_taulu = IntJoukko._alusta_joukko_operaatio(a, b)
        
        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y, a_taulu, b_taulu = IntJoukko._alusta_joukko_operaatio(a, b)
        
        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z, a_taulu, b_taulu = IntJoukko._alusta_joukko_operaatio(a, b)
        
        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return f"{{{str(self.lukujono[0])}}}"
        else:
            alkiot=""
            for i in range(0, self.alkioiden_lkm):
                alkiot += f'{str(self.lukujono[i])}{", " if i != self.alkioiden_lkm -1 else ""}'

            return f'{{{alkiot}}}'
