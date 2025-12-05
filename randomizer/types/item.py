from smrpgpatchbuilder.datatypes.items.classes import (
    Item as ItemBase,
    RegularItem as RegularItemBase,
    Weapon as WeaponBase,
    Armor as ArmorBase,
    Accessory as AccessoryBase,
)
from typing import Optional

class Item(ItemBase):
    _remake_name: Optional[str] = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._item_name

class Weapon(WeaponBase, Item):
    pass

class Armor(ArmorBase, Item):
    pass

class Accessory(AccessoryBase, Item):
    pass

class RegularItem(RegularItemBase, Item):
    pass