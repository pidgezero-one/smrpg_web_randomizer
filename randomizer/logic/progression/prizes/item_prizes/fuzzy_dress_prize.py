from __future__ import annotations
from randomizer.data.items.items import (FuzzyDressItem)
from randomizer.data.physical_objects.bosses import (SPR0231_DRESS)
from randomizer.data.physical_objects.items import (DressObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FuzzyDressPrize(ItemPrize):
    item = FuzzyDressItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Dress", description="Made of the finest fleece."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = DressObject
    _packet_data = (SPR0231_DRESS, 0)


__all__ = ["FuzzyDressPrize"]
