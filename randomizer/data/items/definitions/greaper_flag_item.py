from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class GreaperFlagItem(RegularItem):
    """Greaper Flag item class"""
    _item_name: str = "Greaper Flag"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 163
    _description: str = " It's a\n Greaper Flag"
    _price: int = 0
    _inflict_type = None


__all__ = ["GreaperFlagItem"]
