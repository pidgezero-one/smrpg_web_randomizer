from __future__ import annotations
from randomizer.data.items.items import (AntidotePinItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class AntidotePinPrize(ItemPrize):
    item = AntidotePinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Button", description="Looks like an environmentalist\n thing."
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["AntidotePinPrize"]
