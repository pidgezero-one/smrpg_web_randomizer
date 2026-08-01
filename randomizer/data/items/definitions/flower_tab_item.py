from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class FlowerTabItem(RegularItem):
    """Flower Tab item class"""
    _item_name: str = "Flower Tab"
    _prefix = ItemPrefix.EMPTY_SPACE

    _text_shop_menu = "Flower Tab......."

    _item_id: int = 115
    _description: str = " Raises Flower\n Pts. by 1"
    _inflict: int = 1
    _price: int = 200
    _inflict_type = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["FlowerTabItem"]
