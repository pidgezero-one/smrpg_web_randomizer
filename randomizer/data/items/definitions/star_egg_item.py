from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class StarEggItem(RegularItem):
    """Star Egg item class"""
    _item_name: str = "Star Egg"
    _prefix = ItemPrefix.BOMB

    _item_id: int = 176
    _description: str = " Reusable battle\n item"
    _inflict: int = 100
    _price: int = 2
    _inflict_type = None
    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["StarEggItem"]
