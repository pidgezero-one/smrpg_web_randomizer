from __future__ import annotations
from randomizer.data.items.items import (EnergizerItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (PDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class EnergizerPrize(ItemPrize):
    item = EnergizerItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = PDrinkObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 3)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["EnergizerPrize"]
