class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьет кого-то')
        self.endurance -= 5

    def walk(self):
        print(f'{self.name} идет')

    def info(self):
        print(f'имя воина - {self.name}')
        print(f'сила - {self.power}')
        print(f'выносливость - {self.endurance}')
        print(f'цвет волос - {self.hair_color}')
        