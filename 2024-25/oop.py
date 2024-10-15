import random

class Cat:
    def __init__(self, name, 
    power = random.randint(20, 100), 
    hp = random.randint(20, 100),
    agility = random.randint(20, 100),
    enemy = None):
        self.__name = name
        self.power = power
        self.hp = hp
        self.agility = agility
        self.enemy = enemy
    
    def __str__(self):
        return self.__name

    def setDamage(self, cat_hit):
        damage = random.randint(1, self.power)
        
        cat_hit.getDamage(damage, self.power, self)
    
    def getDamage(self, damage, maxpower, abuser):
        final_damage = int( (1 - (self.agility / 100)) * (damage + (maxpower - self.agility)))
        if final_damage < 0:
            final_damage = 0

        self.hp -= final_damage

        self.enemy = abuser.__name

        if self.hp <= 0:
            self.hp = 0
            nameR = self.__name + 'a'
            print(self.enemy, 'прибил', nameR)

        elif final_damage == 0:
            nameR = self.__name + 'y'
            print(self.enemy, 'не попал по', nameR)
        
        elif final_damage >= (self.hp // 2):
            nameR = self.__name + 'a'
            print(self.enemy, 'сильно ударил', nameR)

        else:
            nameR = self.__name + 'a'
            print(self.enemy, 'ударил', nameR)

    def meow(self):
        print(self.__name, ': Мяу!')

    def sayHello(self):
        print(self.__name, ': Меня зовут', self.__name)


barsik = Cat('Барсик')
barsik.__name = 'Мурзик'
print(barsik)