from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class FroggieDrinkItem(RegularItem):
    """FroggieDrink item class"""
    _item_name: str = "FroggieDrink"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "FroggieDrink......"
    _remake_text_shop_menu = "Tadpola Cola......"

    _item_id: int = 119
    _description: str = " Party recovers\n 30 HP"
    _inflict: int = 30
    _price: int = 16
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True

    _remake_name = "Tadpola Cola"


__all__ = ["FroggieDrinkItem"]
