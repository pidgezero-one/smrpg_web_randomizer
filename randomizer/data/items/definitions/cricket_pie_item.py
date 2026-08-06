from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CricketPieItem(RegularItem):
    """Cricket Pie item class"""
    _item_name: str = "Cricket Pie"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 130
    _description: str = " A tasty looking\n pie"
    _price: int = 0
    _inflict_type = None


__all__ = ["CricketPieItem"]
