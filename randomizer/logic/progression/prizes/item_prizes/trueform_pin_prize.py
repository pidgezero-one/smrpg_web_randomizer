from __future__ import annotations
from randomizer.data.items.items import (TrueformPinItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class TrueformPinPrize(ItemPrize):
    item = TrueformPinItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Button",
        description="For someone who doesn't like\n scarecrows.",
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["TrueformPinPrize"]
