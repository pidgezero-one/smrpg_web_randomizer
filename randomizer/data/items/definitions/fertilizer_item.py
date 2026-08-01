from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class FertilizerItem(RegularItem):
    """Fertilizer item class"""
    _item_name: str = "Fertilizer"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 159
    _description: str = " Nutrients!"
    _price: int = 0
    _inflict_type = None


__all__ = ["FertilizerItem"]
