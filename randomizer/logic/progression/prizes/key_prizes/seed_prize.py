from __future__ import annotations
from randomizer.data.items.items import (SeedItem)
from randomizer.data.physical_objects.bosses import (SPR0253_BERRY)
from randomizer.data.physical_objects.items import (BerryObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class SeedPrize(ItemPrize, KeyPrize):
    item = SeedItem
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Seed", description="I wonder what will grow from it?"
    )
    _model = BerryObject
    _packet_data = (SPR0253_BERRY, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["SeedPrize"]
