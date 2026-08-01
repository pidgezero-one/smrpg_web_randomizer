from __future__ import annotations
from randomizer.data.items.items import (HandGunItem)
from randomizer.data.physical_objects.bosses import (SPR0228_GUN_PACKET)
from randomizer.data.physical_objects.items import (GunObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class HandGunPrize(ItemPrize):
    item = HandGunItem
    _nickname = TreasureHunterNickname(
        nickname="BB Gun", description="I'll throw in some ammo, too."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = GunObject
    _packet_data = (SPR0228_GUN_PACKET, 0)


__all__ = ["HandGunPrize"]
