from operaatio import Operaatio

class Erotus(Operaatio):
    
    def suorita(self):
        arvo = self._kasittele_syote()
        return self.logiikka.miinus(arvo)
