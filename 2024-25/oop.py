class Cat:
    def __init__(self, name):
        self.name = name
        print(self.name, ': Я родился!')

    def meow(self):
        print(self.name, ': Мяу!')

    def sayHello(self):
        print(self.name, ': Меня зовут', self.name)

import random

names = ['Барсик', 'Мурзик', 'Тишка', 'Тимофей', 'Багира', 'Рыжик']
cats = []
for i in range(3):
    cats.append(Cat(random.choice(names)))

for cat in cats:
    cat.sayHello()