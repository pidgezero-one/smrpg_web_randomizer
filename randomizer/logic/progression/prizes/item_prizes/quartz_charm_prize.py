from __future__ import annotations
from randomizer.data.items.items import (QuartzCharmItem)
from randomizer.data.physical_objects.bosses import (SPR0209_SHINY_STONE)
from randomizer.data.physical_objects.items import (CrystalObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class QuartzCharmPrize(ItemPrize):
    item = QuartzCharmItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    _monstro_shuffle = True
    _model = CrystalObject
    _packet_data = (SPR0209_SHINY_STONE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["QuartzCharmPrize"]
