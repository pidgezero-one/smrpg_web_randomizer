from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class RareFrogCoinItem(RegularItem):
    """RareFrogCoin item class"""
    _item_name: str = "RareFrogCoin"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 128
    _description: str = " It's a Frog Coin\n from Frogfucius!"
    _price: int = 0
    _inflict_type = None

    _remake_name = "Special Coin"


__all__ = ["RareFrogCoinItem"]
