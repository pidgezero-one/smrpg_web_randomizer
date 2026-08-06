from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class AltoCardItem(RegularItem):
    """Alto Card item class"""
    _item_name: str = "Alto Card"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 151
    _description: str = " A membership\n card for the\n Juice Bar"
    _price: int = 0
    _inflict_type = None


__all__ = ["AltoCardItem"]
