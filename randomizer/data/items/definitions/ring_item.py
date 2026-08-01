from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class RingItem(RegularItem):
    """Ring item class"""
    _item_name: str = "Ring"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 169
    _description: str = " An expensive\n ring!"
    _price: int = 0
    _inflict_type = None


__all__ = ["RingItem"]
