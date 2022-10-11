class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        print('healed ' + str(self.hp + 100))
    def greetings(self):
        print('my name is ' + self.name)
    def two_damage(self):
        print('damage boosted: ' + str(self.damage * 2))
    def True_phrase(self):
        self.fly = False
        if self.fly == False:
            self.fly = True
            print(f'fly in the freedom')

# gon = Hero(name='Gon ', nickname='wednsday ', hp=100, damage=10)
# print(gon.name, gon.nickname, gon.hp, gon.damage)
# gon.heal()

# frik = Hero(name='Frik ', nickname='monday ', hp=200, damage=100)
# print(frik.name,frik.nickname,frik.hp,frik.damage)
# frik.two_damage()

# john = Hero(name='John ', nickname='sunday ', hp=150, damage=110)
# print(john.name,john.nickname,john.hp,john.damage)
# frik.greetings()

# donna = Hero(name='Donna ', nickname='tuesday ', hp=130, damage=190)
# print(donna.name,donna.nickname,donna.hp,donna.damage)
# donna.brand_phrase()
