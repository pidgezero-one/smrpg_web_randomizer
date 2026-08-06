from __future__ import annotations
from randomizer.data.items.items import (WorkPantsItem)
from randomizer.data.physical_objects.bosses import (SPR0229_PANTS)
from randomizer.data.physical_objects.items import (PantsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class WorkPantsPrize(ItemPrize):
    item = WorkPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Stained Pants", description="They look a bit worn out."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = PantsObject
    _packet_data = (SPR0229_PANTS, 0)


__all__ = ["WorkPantsPrize"]
