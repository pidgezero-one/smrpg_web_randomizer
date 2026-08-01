from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CrystalShardItem(RegularItem):
    """Crystal Shard item class"""
    _item_name: str = "CrystalShard"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 149
    _description: str = " A symbol\n of ultimate\n strength"
    _price: int = 0
    _inflict_type = None


__all__ = ["CrystalShardItem"]
