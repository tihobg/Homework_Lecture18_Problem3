from animal import Animal


class Cat(Animal):
    def __init__(self, age, name, gender):
        super().__init__(age, name, gender)

    def set_animal_voice(self):
        sound = 'Miauuu!'
        return sound
