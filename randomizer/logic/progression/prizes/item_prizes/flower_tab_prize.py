from __future__ import annotations
from randomizer.data.items.items import (FlowerTabItem)
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (FlowerItemObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class FlowerTabPrize(ItemPrize):
    item = FlowerTabItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Capsule", description="You collect these, right?"
    )
    _model = FlowerItemObject
    _packet_data = (SPR0195_FLOWER, 0)


__all__ = ["FlowerTabPrize"]
