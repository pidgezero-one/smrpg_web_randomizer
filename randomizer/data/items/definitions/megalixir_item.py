from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class MegalixirItem(RegularItem):
    """Megalixir item class"""
    _item_name: str = "Megalixir"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Megalixir.........."
    _remake_text_shop_menu = "Finless Cola......."

    _item_id: int = 122
    _description: str = " Party recovers\n 150 HP"
    _inflict: int = 150
    _price: int = 120
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True

    _remake_name = "Finless Cola"


__all__ = ["MegalixirItem"]
