from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BrightCardItem(RegularItem):
    """Bright Card item class"""
    _item_name: str = "Bright Card"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 174
    _description: str = " A member's card\n for the casino"
    _price: int = 0
    _inflict_type = None


__all__ = ["BrightCardItem"]
