from __future__ import annotations
from randomizer.data.items.items import (BrightCardItem)
from randomizer.data.physical_objects.bosses import (SPR0206_CARD)
from randomizer.data.physical_objects.items import (CardObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class BrightCardPrize(ItemPrize, KeyPrize):
    item = BrightCardItem
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject
    _packet_data = (SPR0206_CARD, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["BrightCardPrize"]
