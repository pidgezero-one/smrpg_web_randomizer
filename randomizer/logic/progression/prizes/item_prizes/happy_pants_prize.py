from __future__ import annotations
from randomizer.data.items.items import (HappyPantsItem)
from randomizer.data.physical_objects.bosses import (SPR0229_PANTS)
from randomizer.data.physical_objects.items import (PantsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class HappyPantsPrize(ItemPrize):
    item = HappyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Pants", description="They're all the rage these days!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = PantsObject
    _packet_data = (SPR0229_PANTS, 0)


__all__ = ["HappyPantsPrize"]
