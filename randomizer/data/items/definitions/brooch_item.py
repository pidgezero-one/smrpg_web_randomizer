from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BroochItem(RegularItem):
    """Brooch item class"""
    _item_name: str = "Brooch"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 168
    _description: str = " A shiny brooch!"
    _price: int = 0
    _inflict_type = None


__all__ = ["BroochItem"]
