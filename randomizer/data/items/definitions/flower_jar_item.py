from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class FlowerJarItem(RegularItem):
    """Flower Jar item class"""
    _item_name: str = "Flower Jar"
    _prefix = ItemPrefix.EMPTY_SPACE

    _text_shop_menu = "Flower Jar......."

    _item_id: int = 116
    _description: str = " Raises Flower\n Pts. by 3"
    _inflict: int = 3
    _price: int = 600
    _inflict_type = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["FlowerJarItem"]
