def add(*args):
    y = 0
    for n in args:
        y += n
    return y


x = add(1, 5, 6, 25, 110)
print(x)


class Cat:
    def __init__(self, **kw):
        self.paw = kw.get("paw")
        self.eyes = kw.get("eyes")


t = [1, 3, 5]
my_cat = Cat(paw=t[0])
print(my_cat.paw)


