from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class HoneySyrupItem(RegularItem):
    """Honey Syrup item class"""
    _item_name: str = "Honey Syrup"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Honey Syrup......"

    _item_id: int = 99
    _description: str = " Recovers 10\n Flower Pts."
    _inflict: int = 10
    _price: int = 10
    _inflict_type = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _overworld_menu_fill_hp: bool = True
    _one_side_only: bool = True


__all__ = ["HoneySyrupItem"]
