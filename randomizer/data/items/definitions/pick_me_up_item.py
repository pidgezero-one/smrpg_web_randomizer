from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class PickMeUpItem(RegularItem):
    """Pick Me Up item class"""
    _item_name: str = "Pick Me Up"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Pick Me Up......."

    _item_id: int = 102
    _description: str = " Revives downed\n allies"
    _price: int = 5
    _inflict_type = InflictFunction.REVIVE
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _koed_target_only: bool = True
    _one_side_only: bool = True


__all__ = ["PickMeUpItem"]
