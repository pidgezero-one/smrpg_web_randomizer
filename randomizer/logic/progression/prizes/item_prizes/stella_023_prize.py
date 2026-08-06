from __future__ import annotations
from randomizer.data.items.items import (Stella023Item)
from randomizer.data.physical_objects.bosses import (SPR0226_TINY_STAR)
from randomizer.data.physical_objects.items import (GunObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class Stella023Prize(ItemPrize):
    item = Stella023Item
    _nickname = TreasureHunterNickname(
        nickname="Cool Gun", description="Why does it remind me of a train?"
    )
    remake_only = True
    _monstro_shuffle = True
    _model = GunObject
    _packet_data = (SPR0226_TINY_STAR, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["Stella023Prize"]
