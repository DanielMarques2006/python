class Humano:
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = "homo Neanderthalennsis"

@staticmethod
def especies():
    adjectivos = ("Habilis", "Erectus", "Neanderthalennsis", 
    "Sapiens")
    return ("Australopitecto",) + tuple(f"Homo {adj}" for adj in adjectivos)

@classmethod
def is_evoluido(cls):
    return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == "__main__":
   jose = HomoSapiens("Jose")
   gronk = Neanderthal("Gronk")
   print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
   print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')