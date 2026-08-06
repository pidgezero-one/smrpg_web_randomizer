from __future__ import annotations
from randomizer.data.items.items import (FireworksItem)
from randomizer.data.physical_objects.bosses import (SPR0226_TINY_STAR)
from randomizer.data.physical_objects.items import (TinyStarObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RegularFireworksPrize(ItemPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.RARE
    _model = TinyStarObject
    _packet_data = (SPR0226_TINY_STAR, 0)


__all__ = ["RegularFireworksPrize"]
