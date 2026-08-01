from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class ElderKeyItem(RegularItem):
    """Elder Key item class"""
    _item_name: str = "Elder Key"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 141
    _description: str = " The key to the\n Ancestor Hall"
    _price: int = 0
    _inflict_type = None


__all__ = ["ElderKeyItem"]
