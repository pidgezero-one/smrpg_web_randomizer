from __future__ import annotations
from randomizer.data.items.items import (MegaPantsItem)
from randomizer.data.physical_objects.bosses import (SPR0229_PANTS)
from randomizer.data.physical_objects.items import (PantsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MegaPantsPrize(ItemPrize):
    item = MegaPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia.",
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = PantsObject
    _packet_data = (SPR0229_PANTS, 0)


__all__ = ["MegaPantsPrize"]
