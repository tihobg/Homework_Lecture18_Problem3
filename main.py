from dog import Dog
from cat import Cat
from frog import Frog
from kitten import Kitten
from tomcat import Tomcat

list_animal_data = []
while True:
    try:
        num_animals = int(input('Please, enter the total number of animals!\n'))
        break
    except ValueError:
        print('Not a number!')
        print('Try again!')
for i in range(num_animals):
    animal_data = input('Please, enter animal data!\n')
    list_animal_data.append(animal_data)
for i in range(num_animals):
    if list_animal_data[i][:3] == 'Dog':
        dog = Dog(list_animal_data[i][1], list_animal_data[i][2], list_animal_data[i][3])
        print(f"{i + 1} {list_animal_data[i]} {dog.set_animal_voice()}")
    elif list_animal_data[i][:3] == 'Cat':
        cat = Cat(list_animal_data[i][1], list_animal_data[i][2], list_animal_data[i][3])
        print(f"{i + 1} {list_animal_data[i]} {cat.set_animal_voice()}")
    elif list_animal_data[i][:4] == 'Frog':
        frog = Frog(list_animal_data[i][1], list_animal_data[i][2], list_animal_data[i][3])
        print(f"{i + 1} {list_animal_data[i]} {frog.set_animal_voice()}")
    elif list_animal_data[i][:6] == 'Kitten':
        kitten = Kitten(list_animal_data[i][1], list_animal_data[i][2], list_animal_data[i][3])
        print(f"{i + 1} {list_animal_data[i]} {kitten.set_animal_voice()}")
    elif list_animal_data[i][:6] == 'Kitten':
        tomcat = Tomcat(list_animal_data[i][1], list_animal_data[i][2], list_animal_data[i][3])
        print(f"{i + 1} {list_animal_data[i]} {tomcat.set_animal_voice()}")
