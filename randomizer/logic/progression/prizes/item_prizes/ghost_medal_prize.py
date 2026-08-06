from __future__ import annotations
from randomizer.data.items.items import (GhostMedalItem)
from randomizer.data.physical_objects.bosses import (SPR0236_COIN_STATIC_SMALL)
from randomizer.data.physical_objects.items import (SmallCoinItemObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class GhostMedalPrize(ItemPrize):
    item = GhostMedalItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY
    _model = SmallCoinItemObject
    _packet_data = (SPR0236_COIN_STATIC_SMALL, 0)


__all__ = ["GhostMedalPrize"]
