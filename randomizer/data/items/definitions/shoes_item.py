from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class ShoesItem(RegularItem):
    """Shoes item class"""
    _item_name: str = "Shoes"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 167
    _description: str = " There's no\n place like home"
    _price: int = 0
    _inflict_type = None


__all__ = ["ShoesItem"]
