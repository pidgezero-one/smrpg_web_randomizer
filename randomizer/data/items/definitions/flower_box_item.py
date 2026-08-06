from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    InflictFunction,
    ItemPrefix,
    OverworldMenuBehaviour,
)


class FlowerBoxItem(RegularItem):
    """Flower Box item class"""
    _item_name: str = "Flower Box"
    _prefix = ItemPrefix.EMPTY_SPACE

    _text_shop_menu = "Flower Box......."

    _item_id: int = 117
    _description: str = " Raises Flower\n Pts. by 5"
    _inflict: int = 5
    _price: int = 1000
    _inflict_type = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True
    _overworld_menu_behaviour: OverworldMenuBehaviour = OverworldMenuBehaviour.LEAD_TO_FP
    _can_target_others: bool = True
    _one_side_only: bool = True


__all__ = ["FlowerBoxItem"]
