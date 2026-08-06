from __future__ import annotations
from randomizer.data.items.items import (CricketJamItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (GreenJuiceObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class CricketJamPrize(ItemPrize, KeyPrize):
    item = CricketJamItem
    _nickname = TreasureHunterNickname(
        nickname="Green Jelly", description="I wonder what flavor it is?"
    )
    _model = GreenJuiceObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 2)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["CricketJamPrize"]
