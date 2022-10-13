class human:
    age = 11
    name = 12
    growth= 111
    def __new__(cls, age = 11, name = 'gom', growth = 12):
        print(age, name, growth)
        return super().__new__(cls)
gom = human()
print(gom)
