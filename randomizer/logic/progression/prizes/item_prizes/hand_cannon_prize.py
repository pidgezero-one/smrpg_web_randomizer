from __future__ import annotations
from randomizer.data.items.items import (HandCannonItem)
from randomizer.data.physical_objects.bosses import (SPR0228_GUN_PACKET)
from randomizer.data.physical_objects.items import (GunObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class HandCannonPrize(ItemPrize):
    item = HandCannonItem
    _nickname = TreasureHunterNickname(
        nickname="Cannon Launcher", description="You need strong elbows for this!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = GunObject
    _packet_data = (SPR0228_GUN_PACKET, 0)


__all__ = ["HandCannonPrize"]
