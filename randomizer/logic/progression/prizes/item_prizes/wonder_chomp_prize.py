from __future__ import annotations
from randomizer.data.items.items import (WonderChompItem)
from randomizer.data.physical_objects.bosses import (SPR0245_CHOMP_BALL)
from randomizer.data.physical_objects.items import (ChompObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class WonderChompPrize(ItemPrize):
    item = WonderChompItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Chomp",
        description="It's hungry to stir up some BIG\n trouble.",
    )
    remake_only = True
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = ChompObject
    _packet_data = (SPR0245_CHOMP_BALL, 0)


__all__ = ["WonderChompPrize"]
