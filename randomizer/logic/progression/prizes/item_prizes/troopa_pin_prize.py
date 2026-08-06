from __future__ import annotations
from randomizer.data.items.items import (TroopaPinItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (SmallCoinItemObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class TroopaPinPrize(ItemPrize):
    item = TroopaPinItem
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _model = SmallCoinItemObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["TroopaPinPrize"]
