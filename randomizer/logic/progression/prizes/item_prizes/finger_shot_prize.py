from __future__ import annotations
from randomizer.data.items.items import (FingerShotItem)
from randomizer.data.physical_objects.bosses import (SPR0228_GUN_PACKET)
from randomizer.data.physical_objects.items import (GunObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FingerShotPrize(ItemPrize):
    item = FingerShotItem
    _nickname = TreasureHunterNickname(
        nickname="Pellet Shooter", description="It was probably owned by a kid."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = GunObject
    _packet_data = (SPR0228_GUN_PACKET, 0)


__all__ = ["FingerShotPrize"]
