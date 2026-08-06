from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CastleKey1Item(RegularItem):
    """Castle Key 1 item class"""
    _item_name: str = "Castle Key 1"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 132
    _description: str = " It's a\n Castle Key"
    _price: int = 0
    _inflict_type = None


__all__ = ["CastleKey1Item"]
