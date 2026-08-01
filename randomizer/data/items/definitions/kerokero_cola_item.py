from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class KerokeroColaItem(RegularItem):
    """KerokeroCola item class"""
    _item_name: str = "KerokeroCola"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Kerokero Cola...."
    _remake_text_shop_menu = "Croaka Cola......"

    _item_id: int = 108
    _description: str = " All members\n recover fully"
    _price: int = 400
    _inflict_type = InflictFunction.RESTORE_ALL_HP_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_hp: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True

    _remake_name = "Croaka Cola"


__all__ = ["KerokeroColaItem"]
