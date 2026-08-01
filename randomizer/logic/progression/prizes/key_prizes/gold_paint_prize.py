from __future__ import annotations
from randomizer.data.enemies.enemies import (GoldPaintItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (YellowJuiceObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class GoldPaintPrize(ItemPrize, KeyPrize):
    item = GoldPaintItem
    _nickname = TreasureHunterNickname(
        nickname="Chrome Coat", description="It'll make you look shiny!"
    )
    _model = YellowJuiceObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 2)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["GoldPaintPrize"]
