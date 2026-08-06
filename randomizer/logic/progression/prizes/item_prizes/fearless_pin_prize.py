from __future__ import annotations
from randomizer.data.items.items import (FearlessPinItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FearlessPinPrize(ItemPrize):
    item = FearlessPinItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Button", description="Who you gonna call?\n GHOSTBUSTERS!"
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["FearlessPinPrize"]
