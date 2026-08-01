from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class YoshiCandyItem(RegularItem):
    """Yoshi Candy item class"""
    _item_name: str = "Yoshi Candy"
    _prefix = ItemPrefix.DOT

    _text_shop_menu = "Yoshi Candy......"

    _item_id: int = 118
    _description: str = "Recovers 100 HP"
    _inflict: int = 100
    _price: int = 140
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["YoshiCandyItem"]
