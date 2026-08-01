from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class WiltShroomItem(RegularItem):
    """Wilt Shroom item class"""
    _item_name: str = "Wilt Shroom"
    _prefix = ItemPrefix.CONSUMABLE

    _item_id: int = 155
    _description: str = " It's wilted..."
    _inflict: int = 10
    _price: int = 8
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["WiltShroomItem"]
