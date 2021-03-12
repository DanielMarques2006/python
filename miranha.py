class Animal:
    @property
    def capacidades(self):
        return ("dormir", "comer", "beber")


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("amar", "falar", "estudar")

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("fazer teias", "andar pelas paredes")

class Miranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ("bater em bandidos", "atirar teia entre predios")

if __name__ == "__main__":
    jonh = Homem()
    print(f'Jonh: {jonh.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    miranha = Miranha()
    print(f'Miranha: {miranha.capacidades}')