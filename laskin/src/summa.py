from operaatio import Operaatio

class Summa(Operaatio):
    
    def suorita(self):
        arvo = self._kasittele_syote()
        return self.logiikka.plus(arvo)
