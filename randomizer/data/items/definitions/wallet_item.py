from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class WalletItem(RegularItem):
    """Wallet item class"""
    _item_name: str = "Wallet"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 129
    _description: str = " A fat wallet"
    _price: int = 0
    _inflict_type = None


__all__ = ["WalletItem"]
