class Participante:
    def __init__(self, alias, simbolo):
        self.alias = alias
        self.simbolo = simbolo
    
    def nombre(self):
        return self.alias
    
    def ficha(self):
        return self.simbolo
