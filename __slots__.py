import sys


class Car(object):
    __slots__ = ["color", "max_speed", "model"]
    def __init__(self, color, max_speed, model):
        self.color = color
        self.max_speed = max_speed
        self.model = model

pride = Car("white", 100, 2010)

print(pride.color)
# print(pride.__dict__)
print(sys.getsizeof(pride))


class Car1(object):# object python be onvan yek no dadei negah mishe
    __slots__ = ()
    color = "red"
    max_speed = 120
    model = 2011

c = Car1()

print(sys.getsizeof(c))



