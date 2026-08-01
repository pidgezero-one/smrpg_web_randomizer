from __future__ import annotations
from randomizer.data.items.items import (SpikedLinkItem)
from randomizer.data.physical_objects.bosses import (SPR0245_CHOMP_BALL)
from randomizer.data.physical_objects.items import (ChompObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SpikedLinkPrize(ItemPrize):
    item = SpikedLinkItem
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="This one's got thorns on it."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = ChompObject
    _packet_data = (SPR0245_CHOMP_BALL, 0)


__all__ = ["SpikedLinkPrize"]
