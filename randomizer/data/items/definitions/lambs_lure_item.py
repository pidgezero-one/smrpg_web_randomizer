from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class LambsLureItem(RegularItem):
    """Lambs Lure item class"""
    _item_name: str = "Lamb's Lure"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 143
    _description: str = " Baa, baa..."
    _price: int = 2
    _inflict_type = InflictFunction.INSTANT_DEATH
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True


__all__ = ["LambsLureItem"]
