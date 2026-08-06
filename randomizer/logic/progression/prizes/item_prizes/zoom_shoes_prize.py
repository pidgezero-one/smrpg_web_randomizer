from __future__ import annotations
from randomizer.data.items.items import (ZoomShoesItem)
from randomizer.data.physical_objects.bosses import (SPR0202_SHOES)
from randomizer.data.physical_objects.items import (ShoesObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class ZoomShoesPrize(ItemPrize):
    item = ZoomShoesItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Vans", description="I bet you can run really fast in\n these."
    )
    _monstro_shuffle = True
    _model = ShoesObject
    _packet_data = (SPR0202_SHOES, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["ZoomShoesPrize"]
