from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class MidMushroomItem(RegularItem):
    """Mid Mushroom item class"""
    _item_name: str = "Mid Mushroom"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Mid Mushroom...."

    _item_id: int = 97
    _description: str = " Recovers 80 HP"
    _inflict: int = 80
    _price: int = 20
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["MidMushroomItem"]
