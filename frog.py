from animal import Animal


class Frog(Animal):
    def __init__(self, age, name, gender):
        super().__init__(age, name, gender)

    def set_animal_voice(self):
        sound = 'Kwak!'
        return sound
