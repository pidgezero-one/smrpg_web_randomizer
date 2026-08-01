from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class SopranoCardItem(RegularItem):
    """Soprano Card item class"""
    _item_name: str = "Soprano Card"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 150
    _description: str = " A membership\n card for the\n Juice Bar"
    _price: int = 0
    _inflict_type = None


__all__ = ["SopranoCardItem"]
