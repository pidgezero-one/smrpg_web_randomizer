from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class ExtraShinyStoneItem(RegularItem):
    """Extra Shiny Stone item class"""
    _item_name: str = "X.ShinyStone"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 139
    _description: str = " A very\n pretty stone!"
    _price: int = 0
    _inflict_type = None


__all__ = ["ExtraShinyStoneItem"]
