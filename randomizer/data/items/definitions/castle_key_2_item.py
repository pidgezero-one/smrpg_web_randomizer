from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CastleKey2Item(RegularItem):
    """Castle Key 2 item class"""
    _item_name: str = "Castle Key 2"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 134
    _description: str = " It's a\n Castle Key"
    _price: int = 0
    _inflict_type = None


__all__ = ["CastleKey2Item"]
