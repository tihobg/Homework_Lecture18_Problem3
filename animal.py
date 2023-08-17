class Animal:
    def __init__(self,
                 name='',
                 age=0,
                 gender=''):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, value):
        self._name = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    def set_animal_voice(self):
        print(f"Each animal make a specific voice!")
