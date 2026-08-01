from __future__ import annotations
from randomizer.data.items.items import (WarFanItem)
from randomizer.data.physical_objects.bosses import (SPR0227_FAN_PACKET)
from randomizer.data.physical_objects.items import (FanObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class WarFanPrize(ItemPrize):
    item = WarFanItem
    _nickname = TreasureHunterNickname(
        nickname="Spiked Fan", description="Pretty, but deadly!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = FanObject
    _packet_data = (SPR0227_FAN_PACKET, 0)


__all__ = ["WarFanPrize"]
