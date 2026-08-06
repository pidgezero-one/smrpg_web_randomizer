from __future__ import annotations
from randomizer.data.items.items import (ChompItem)
from randomizer.data.physical_objects.bosses import (SPR0245_CHOMP_BALL)
from randomizer.data.physical_objects.items import (ChompObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class ChompPrize(ItemPrize):
    item = ChompItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="It's hungry to stir up some trouble."
    )
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = ChompObject
    _packet_data = (SPR0245_CHOMP_BALL, 0)


__all__ = ["ChompPrize"]
