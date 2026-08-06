from __future__ import annotations
from randomizer.data.items.items import (SignalRingItem)
from randomizer.data.physical_objects.bosses import (SPR0196_RING)
from randomizer.data.physical_objects.items import (RingObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SignalRingPrize(ItemPrize):
    item = SignalRingItem
    _nickname = TreasureHunterNickname(
        nickname="Bell Charm", description="I wonder what it can help you find?"
    )
    _model = RingObject
    _packet_data = (SPR0196_RING, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["SignalRingPrize"]
