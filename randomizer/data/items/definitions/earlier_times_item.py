from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class EarlierTimesItem(RegularItem):
    """EarlierTimes item class"""
    _item_name: str = "EarlierTimes"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 126
    _description: str = " Use it to start\n a battle over"
    _price: int = 15
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["EarlierTimesItem"]
