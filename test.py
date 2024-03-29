class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_hero(self):
        print(f'Имя героя: {self.name}')

    def health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Питер Паркер', 'Человек-Паук',
                 'Паучье чутьё', 120, "С большой силой приходит большая ответственность")
hero.name_hero()
hero.health()
print(hero)
print("Длина коронной фразы героя:", len(hero))
