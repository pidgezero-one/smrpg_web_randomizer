from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class DryBonesFlagItem(RegularItem):
    """DryBonesFlag item class"""
    _item_name: str = "DryBonesFlag"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 162
    _description: str = " It's a\n Dry Bones' Flag"
    _price: int = 0
    _inflict_type = None


__all__ = ["DryBonesFlagItem"]
