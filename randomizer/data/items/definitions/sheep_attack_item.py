from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (InflictFunction, ItemPrefix)


class SheepAttackItem(RegularItem):
    """Sheep Attack item class"""
    _item_name: str = "Sheep Attack"
    _prefix = ItemPrefix.QUESTION

    _item_id: int = 136
    _description: str = " Baah, baah..."
    _price: int = 2
    _inflict_type = InflictFunction.INSTANT_DEATH
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["SheepAttackItem"]
