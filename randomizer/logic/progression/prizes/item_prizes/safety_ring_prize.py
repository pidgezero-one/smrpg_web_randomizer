from __future__ import annotations
from randomizer.data.items.items import (SafetyRingItem)
from randomizer.data.physical_objects.bosses import (SPR0196_RING)
from randomizer.data.physical_objects.items import (RingObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SafetyRingPrize(ItemPrize):
    item = SafetyRingItem
    _nickname = TreasureHunterNickname(
        nickname="Protective Charm", description="Never go into battle without it."
    )
    _model = RingObject
    _packet_data = (SPR0196_RING, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["SafetyRingPrize"]
