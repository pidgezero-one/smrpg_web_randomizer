from __future__ import annotations
from randomizer.data.items.items import (DrillClawItem)
from randomizer.data.physical_objects.bosses import (SPR0208_GLOVE)
from randomizer.data.physical_objects.items import (GloveObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class DrillClawPrize(ItemPrize):
    item = DrillClawItem
    _nickname = TreasureHunterNickname(
        nickname="Drilling Appendage",
        description="I bet you could do some real damage\n with this.",
    )
    _model = GloveObject
    _packet_data = (SPR0208_GLOVE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["DrillClawPrize"]
