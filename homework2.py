from homewr1 import Hero


class air(Hero):
    dop = 'air'

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __gen_x(self):
        pass


class earth(Hero):
    pod = 'earth'

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __gen_x(self):
        pass


class cosmic(Hero):
    tod = 'space'

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __gen_x(self):
        pass



ear = earth('semo', 'hopper', 10, 1)
print(ear.name, ear.nickname, ear.fly)
print(ear.True_phrase())

aer = air('erno', 'frierr', 12, 2)
print(aer.name, aer.nickname, aer.fly)

cos = cosmic('noer', 'post', 22, 4)
print(cos.name, cos.nickname, cos.hp, cos.damage)
