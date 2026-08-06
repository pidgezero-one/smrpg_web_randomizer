from __future__ import annotations
from randomizer.data.items.items import (JumpShoesItem)
from randomizer.data.physical_objects.bosses import (SPR0202_SHOES)
from randomizer.data.physical_objects.items import (ShoesObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class JumpShoesPrize(ItemPrize):
    item = JumpShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Brown Clogs", description="Check out the thick soles!"
    )
    _model = ShoesObject
    _packet_data = (SPR0202_SHOES, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["JumpShoesPrize"]
