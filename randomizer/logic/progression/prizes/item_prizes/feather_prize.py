from __future__ import annotations
from randomizer.data.items.items import (FeatherItem)
from randomizer.data.physical_objects.bosses import (SPR0252_FEATHER)
from randomizer.data.physical_objects.items import (FeatherObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FeatherPrize(ItemPrize):
    item = FeatherItem
    _nickname = TreasureHunterNickname(
        nickname="Fluttering Quill", description="It's pretty exotic, isn't it?"
    )
    _model = FeatherObject
    _packet_data = (SPR0252_FEATHER, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["FeatherPrize"]
