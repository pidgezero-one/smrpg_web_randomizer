from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class MaxMushroomItem(RegularItem):
    """Max Mushroom item class"""
    _item_name: str = "Max Mushroom"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Max Mushroom...."

    _item_id: int = 98
    _description: str = "Recovers all HP"
    _inflict: int = 255
    _price: int = 78
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["MaxMushroomItem"]
