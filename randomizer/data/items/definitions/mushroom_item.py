from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class MushroomItem(RegularItem):
    """Mushroom item class"""
    _item_name: str = "Mushroom"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Mushroom........"

    _item_id: int = 96
    _description: str = " Recovers 30 HP"
    _inflict: int = 30
    _price: int = 4
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["MushroomItem"]
