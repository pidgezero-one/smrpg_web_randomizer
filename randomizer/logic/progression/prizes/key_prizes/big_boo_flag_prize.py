from __future__ import annotations
from randomizer.data.items.items import (BigBooFlagItem)
from randomizer.data.physical_objects.bosses import (SPR0206_CARD)
from randomizer.data.physical_objects.items import (CardObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class BigBooFlagPrize(ItemPrize, KeyPrize):
    item = BigBooFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?",
    )
    _model = CardObject
    _packet_data = (SPR0206_CARD, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["BigBooFlagPrize"]
