from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class ElixirItem(RegularItem):
    """Elixir item class"""
    _item_name: str = "Elixir"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Elixir............."
    _remake_text_shop_menu = "Frogleg Cola......"

    _item_id: int = 121
    _description: str = " Party recovers\n 80 HP"
    _inflict: int = 80
    _price: int = 48
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True

    _remake_name = "Frogleg Cola"


__all__ = ["ElixirItem"]
