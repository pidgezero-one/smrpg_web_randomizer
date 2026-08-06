from __future__ import annotations
from randomizer.data.items.items import (ScroogeRingItem)
from randomizer.data.physical_objects.bosses import (SPR0196_RING)
from randomizer.data.physical_objects.items import (RingObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class ScroogeRingPrize(ItemPrize):
    item = ScroogeRingItem
    _nickname = TreasureHunterNickname(
        nickname="Mage Totem", description="It might help with spellcasting."
    )
    _model = RingObject
    _packet_data = (SPR0196_RING, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["ScroogeRingPrize"]
