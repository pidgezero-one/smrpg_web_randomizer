from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class ShedKeyItem(RegularItem):
    """Shed Key item class"""
    _item_name: str = "Shed Key"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 142
    _description: str = " The key\n to the shed\n in Seaside Town"
    _price: int = 0
    _inflict_type = None


__all__ = ["ShedKeyItem"]
