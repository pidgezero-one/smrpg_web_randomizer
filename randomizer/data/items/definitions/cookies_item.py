from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CookiesItem(RegularItem):
    """Cookies item class"""
    _item_name: str = "Cookies"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 165
    _description: str = " Give these\n to Boshi\n for a race"
    _price: int = 0
    _inflict_type = None


__all__ = ["CookiesItem"]
