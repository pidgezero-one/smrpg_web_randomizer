from __future__ import annotations
from randomizer.data.items.items import (LazyShellItem2)
from randomizer.data.physical_objects.bosses import (SPR0249_RED_SHELL)
from randomizer.data.physical_objects.items import (RedShellObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class LazyShellArmorPrize(ItemPrize):
    item = LazyShellItem2
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _monstro_shuffle = True
    _model = RedShellObject
    _packet_data = (SPR0249_RED_SHELL, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR


__all__ = ["LazyShellArmorPrize"]
