from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BigBooFlagItem(RegularItem):
    """Big Boo Flag item class"""
    _item_name: str = "Big Boo Flag"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 161
    _description: str = " It's a\n Big Boo Flag"
    _price: int = 0
    _inflict_type = None

    _remake_name = "Boo Flag"


__all__ = ["BigBooFlagItem"]
