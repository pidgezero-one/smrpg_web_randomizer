from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class PureWaterItem(RegularItem):
    """Pure Water item class"""
    _item_name: str = "Pure Water"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Pure Water......."

    _item_id: int = 110
    _description: str = " Defeats ghosts\n in a wink"
    _price: int = 150
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True


__all__ = ["PureWaterItem"]
