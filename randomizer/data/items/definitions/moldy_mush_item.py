from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class MoldyMushItem(RegularItem):
    """Moldy Mush item class"""
    _item_name: str = "Moldy Mush"
    _prefix = ItemPrefix.CONSUMABLE

    _item_id: int = 157
    _description: str = " Gross!\n There's mold\n growing on it."
    _inflict: int = 1
    _price: int = 2
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["MoldyMushItem"]
