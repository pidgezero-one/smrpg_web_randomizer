from __future__ import annotations
from randomizer.data.items.items import (CrystalShardItem)
from randomizer.data.physical_objects.bosses import (SPR0209_SHINY_STONE)
from randomizer.data.physical_objects.items import (CrystalObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class CrystalShardPrize(ItemPrize, KeyPrize):
    item = CrystalShardItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    remake_only = True
    _model = CrystalObject
    _packet_data = (SPR0209_SHINY_STONE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["CrystalShardPrize"]
