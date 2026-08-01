from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class TenorCardItem(RegularItem):
    """Tenor Card item class"""
    _item_name: str = "Tenor Card"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 152
    _description: str = " A membership\n card for the\n Juice Bar"
    _price: int = 0
    _inflict_type = None


__all__ = ["TenorCardItem"]
