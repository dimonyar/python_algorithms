from datetime import datetime as dt


class Player:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__helth', '__created']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__helth = Player.__HEALTH
        self.__created = dt.now()

    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)

    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Most be int')


x = Player()
print(x.lvl)
x.lvl = 5
print(x.lvl)

Player.set_cls_field(10)
y = Player()
print(y.lvl)

Player.set_cls_field()
y = Player()
print(y.lvl)
y.lvl = 2.2
