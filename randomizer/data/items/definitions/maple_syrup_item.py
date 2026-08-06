from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class MapleSyrupItem(RegularItem):
    """Maple Syrup item class"""
    _item_name: str = "Maple Syrup"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Maple Syrup......"

    _item_id: int = 100
    _description: str = " Recovers 40\n Flower Pts."
    _inflict: int = 40
    _price: int = 30
    _inflict_type = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _overworld_menu_fill_hp: bool = True
    _one_side_only: bool = True


__all__ = ["MapleSyrupItem"]
