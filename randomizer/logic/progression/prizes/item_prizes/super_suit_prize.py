from __future__ import annotations
from randomizer.data.items.items import (SuperSuitItem)
from randomizer.data.physical_objects.bosses import (SPR0230_OVERALLS)
from randomizer.data.physical_objects.items import (OverallsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class SuperSuitPrize(ItemPrize):
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    item = SuperSuitItem
    _nickname = TreasureHunterNickname(
        nickname="Jumpsuit", description="It looks pretty powerful, right?"
    )
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = OverallsObject
    _packet_data = (SPR0230_OVERALLS, 0)


__all__ = ["SuperSuitPrize"]
