from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class LuckyJewelItem(RegularItem):
    """Lucky Jewel item class"""
    _item_name: str = "Lucky Jewel"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 148
    _description: str = " Summons Luck\n at will"
    _price: int = 100
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _one_side_only: bool = True


__all__ = ["LuckyJewelItem"]
