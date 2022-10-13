class summation:
    def __init__(self, num):
        self.num = num
    def __add__(self, other, sun):
        self.sun = other + self.num

class subtraction:
    def __init__(self, num):
        self.num = num
    def __sub__(self, other, su):
        self.su = other - self.num

class division:
    def __init__(self, num, di):
        self.num = num
        self.di = di
    def __truediv__(self, other, di):
        self.di = other / self.num

class multiplication:
    def __init__(self, num):
        self.num = num
    def __mul__(self, other, mu):
        self.mu = other * self.num

class A(multiplication, subtraction, summation, division):
    def __init__(self, num, other, di=int, su=int, sun=int, mu=int):
        super().__init__(num)
        super().__truediv__(other, di)
        super().__sub__(other, su)
        super().__mul__(other, mu)
        super().__add__(other, sun)

fu = A(12, 122)
print(fu.di)
print(fu.mu)
print(fu.su)
print(fu.sun)