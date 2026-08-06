from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class RoomKeyItem(RegularItem):
    """Room Key item class"""
    _item_name: str = "Room Key"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 140
    _description: str = " The key to\n the mine room!"
    _price: int = 0
    _inflict_type = None


__all__ = ["RoomKeyItem"]
