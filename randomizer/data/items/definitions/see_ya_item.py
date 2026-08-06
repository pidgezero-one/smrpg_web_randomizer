from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class SeeYaItem(RegularItem):
    """See Ya item class"""
    _item_name: str = "See Ya"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 123
    _description: str = " Allows you to\n run away from\n battles"
    _price: int = 10
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["SeeYaItem"]
