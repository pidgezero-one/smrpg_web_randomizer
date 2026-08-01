from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class MysteryEggItem(RegularItem):
    """Mystery Egg item class"""
    _item_name: str = "Mystery Egg"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 145
    _description: str = " A product of\n pure love..."
    _price: int = 200
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _one_side_only: bool = True


__all__ = ["MysteryEggItem"]
