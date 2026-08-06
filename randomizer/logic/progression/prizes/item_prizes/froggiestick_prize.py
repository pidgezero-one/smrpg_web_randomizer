from __future__ import annotations
from randomizer.data.items.items import (FroggieStickItem)
from randomizer.data.physical_objects.bosses import (SPR0246_STICK_PACKET)
from randomizer.data.physical_objects.items import (StickObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class FroggiestickPrize(ItemPrize):
    item = FroggieStickItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _monstro_shuffle = True
    _model = StickObject
    _packet_data = (SPR0246_STICK_PACKET, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["FroggiestickPrize"]
