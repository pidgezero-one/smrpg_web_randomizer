from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class RoyalSyrupItem(RegularItem):
    """Royal Syrup item class"""
    _item_name: str = "Royal Syrup"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Royal Syrup......"

    _item_id: int = 101
    _description: str = " Recovers all\n Flower Pts."
    _inflict: int = 99
    _price: int = 101
    _inflict_type = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _overworld_menu_fill_hp: bool = True
    _one_side_only: bool = True


__all__ = ["RoyalSyrupItem"]
