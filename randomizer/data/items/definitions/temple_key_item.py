from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class TempleKeyItem(RegularItem):
    """Temple Key item class"""
    _item_name: str = "Temple Key"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 124
    _description: str = " It's a\n Temple Key"
    _price: int = 0
    _inflict_type = None


__all__ = ["TempleKeyItem"]
