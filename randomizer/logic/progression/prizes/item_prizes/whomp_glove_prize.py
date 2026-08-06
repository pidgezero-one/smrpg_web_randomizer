from __future__ import annotations
from randomizer.data.items.items import (WhompGloveItem)
from randomizer.data.physical_objects.bosses import (SPR0208_GLOVE)
from randomizer.data.physical_objects.items import (GloveObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class WhompGlovePrize(ItemPrize):
    item = WhompGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject
    _packet_data = (SPR0208_GLOVE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["WhompGlovePrize"]
