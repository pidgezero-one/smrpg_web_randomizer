from __future__ import annotations
from randomizer.data.items.items import (UltraHammerItem)
from randomizer.data.physical_objects.bosses import (SPR0247_HAMMER_PACKET)
from randomizer.data.physical_objects.items import (HammerObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class UltraHammerPrize(ItemPrize):
    item = UltraHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = HammerObject
    _packet_data = (SPR0247_HAMMER_PACKET, 0)


__all__ = ["UltraHammerPrize"]
