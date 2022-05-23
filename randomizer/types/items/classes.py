from sympy import pde_separate_add


class Item:
    _id: int

    @property
    def id(self):
        return self._id


class Equipment(Item):
    pass


class Weapon(Equipment):
    _id: int = 0


class Armor(Equipment):
    _id: int = 1


class Accessory(Equipment):
    _id: int = 2
