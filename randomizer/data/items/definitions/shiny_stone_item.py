from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class ShinyStoneItem(RegularItem):
    """Shiny Stone item class"""
    _item_name: str = "Shiny Stone"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 138
    _description: str = " A pretty stone!"
    _price: int = 4
    _inflict_type = None


__all__ = ["ShinyStoneItem"]
