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
        self.health_points **= 2

    def true_phrase(self):
        print('True in the True_phrase')

    def __str__(self):
        return (f'Прозвище: {self.nickname}, '
                f'Суперспособность: {self.superpower}, Здоровье: {self.health_points}')
    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.territory = "air"
        self.damage = damage
        self.fly = fly

    def health(self):
        self.health_points **= 2
        self.fly = True

    def __str__(self):
        return f'{super().__str__()}, Территория: {self.territory}, Урон: {self.damage}, Fly: {self.fly}'


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.territory = "earth"
        self.damage = damage
        self.fly = fly

    def health(self):
        self.health_points **= 2
        self.fly = True

    def __str__(self):
        return f'{super().__str__()}, Территория: {self.territory}, Урон: {self.damage}, Fly: {self.fly}'


class Villain(AirHero):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        target.health_points **= self.damage


air_hero = AirHero('Аанг', 'Аватар',
                   'Воздух', 100,
                   'когда ты убиваешь своего врага, ты сам себя убиваешь...', 50)
air_hero.name_hero()
air_hero.health()
air_hero.true_phrase()
print(air_hero)
print("Длина коронной фразы героя:", len(air_hero))


earth_hero = EarthHero('Тоф', 'Слепой бандит', 'Земля',
                       200, 'Хочешь обнять кого-то – обними дерево.', 100)
earth_hero.name_hero()
earth_hero.health()
earth_hero.true_phrase()
print(earth_hero)
print("Длина коронной фразы героя:", len(earth_hero))


villain = Villain('Озай', 'Король Феникс', 'Огонь',
                  250, 'Скоро мир сгорит во тьме, и тогда новый мир восстанет из пепла!', 70)
villain.name_hero()
villain.health()
villain.true_phrase()
print(villain)
print("Длина коронной фразы злодея:", len(villain))

villain.crit(earth_hero)
print("Здоровье Земного героя после атаки Злодея:", earth_hero.health_points)
