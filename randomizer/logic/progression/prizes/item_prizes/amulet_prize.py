from __future__ import annotations
from randomizer.data.items.items import (AmuletItem)
from randomizer.data.physical_objects.bosses import (SPR0206_CARD)
from randomizer.data.physical_objects.items import (CardObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class AmuletPrize(ItemPrize):
    item = AmuletItem
    _nickname = TreasureHunterNickname(
        nickname="Stinky Charm", description="It'll help you weather the elements."
    )
    _model = CardObject
    _packet_data = (SPR0206_CARD, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["AmuletPrize"]
