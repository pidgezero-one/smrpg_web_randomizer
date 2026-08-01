from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class GoodieBagItem(RegularItem):
    """Goodie Bag item class"""
    _item_name: str = "Goodie Bag"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 125
    _description: str = " It's packed\n full of coins"
    _price: int = 1110
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _one_side_only: bool = True


__all__ = ["GoodieBagItem"]
