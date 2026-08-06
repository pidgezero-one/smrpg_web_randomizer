from __future__ import annotations
from randomizer.data.items.items import (FlowerJarItem)
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (FlowerItemObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class FlowerJarPrize(ItemPrize):
    item = FlowerJarItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Set", description="You collect these, right?"
    )
    _model = FlowerItemObject
    _packet_data = (SPR0195_FLOWER, 0)


__all__ = ["FlowerJarPrize"]
