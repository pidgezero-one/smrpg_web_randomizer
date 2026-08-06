from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class StayVoucherItem(RegularItem):
    """Stay Voucher item class"""
    _item_name: str = "Stay Voucher"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 173
    _description: str = " A hotel ticket"
    _price: int = 0
    _inflict_type = None


__all__ = ["StayVoucherItem"]
