from __future__ import annotations
from randomizer.data.items.items import (DoublePunchItem)
from randomizer.data.physical_objects.bosses import (SPR0208_GLOVE)
from randomizer.data.physical_objects.items import (GloveObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class DoublePunchPrize(ItemPrize):
    item = DoublePunchItem
    _nickname = TreasureHunterNickname(
        nickname="Rocket Launcher",
        description="Be careful, it could take your\n hands clean off.",
    )
    _model = GloveObject
    _packet_data = (SPR0208_GLOVE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["DoublePunchPrize"]
