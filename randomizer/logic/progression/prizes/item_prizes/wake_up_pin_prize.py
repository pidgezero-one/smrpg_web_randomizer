from __future__ import annotations
from randomizer.data.items.items import (WakeUpPinItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class WakeUpPinPrize(ItemPrize):
    item = WakeUpPinItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Button", description="Looks like an anti-fur thing."
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["WakeUpPinPrize"]
