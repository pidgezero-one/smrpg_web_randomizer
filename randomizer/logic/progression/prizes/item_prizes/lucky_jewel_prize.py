from __future__ import annotations
from randomizer.data.items.items import (LuckyJewelItem)
from randomizer.data.physical_objects.bosses import (SPR0209_SHINY_STONE)
from randomizer.data.physical_objects.items import (CrystalObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class LuckyJewelPrize(ItemPrize):
    item = LuckyJewelItem
    _nickname = TreasureHunterNickname(
        nickname="Lucky Jewel",
        description="It’s sure to bring you plenty of\n good luck.",
    )
    _model = CrystalObject
    _packet_data = (SPR0209_SHINY_STONE, 0)


__all__ = ["LuckyJewelPrize"]
