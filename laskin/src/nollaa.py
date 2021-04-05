from operaatio import Operaatio

class Nollaa(Operaatio):
    
    def suorita(self):
        return self.logiikka.nollaa()
