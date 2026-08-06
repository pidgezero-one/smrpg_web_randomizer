from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class RottenMushItem(RegularItem):
    """Rotten Mush item class"""
    _item_name: str = "Rotten Mush"
    _prefix = ItemPrefix.CONSUMABLE

    _item_id: int = 156
    _description: str = " Eeew,\n it's rotten!"
    _inflict: int = 5
    _price: int = 4
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["RottenMushItem"]
