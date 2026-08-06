from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CricketJamItem(RegularItem):
    """Cricket Jam item class"""
    _item_name: str = "Cricket Jam"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 166
    _description: str = " Delicious jam!"
    _price: int = 0
    _inflict_type = None


__all__ = ["CricketJamItem"]
