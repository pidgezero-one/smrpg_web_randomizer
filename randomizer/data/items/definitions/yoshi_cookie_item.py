from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class YoshiCookieItem(RegularItem):
    """Yoshi Cookie item class"""
    _item_name: str = "Yoshi Cookie"
    _prefix = ItemPrefix.DOT

    _text_shop_menu = "Yoshi Cookie......"

    _item_id: int = 109
    _description: str = " Summons Yoshi\n during battle"
    _price: int = 2
    _inflict_type = InflictFunction.ITEM_MORPH
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True


__all__ = ["YoshiCookieItem"]
