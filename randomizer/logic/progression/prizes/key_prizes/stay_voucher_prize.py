from __future__ import annotations
from randomizer.data.items.items import (StayVoucherItem)
from randomizer.data.physical_objects.bosses import (SPR0206_CARD)
from randomizer.data.physical_objects.items import (CardObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class StayVoucherPrize(ItemPrize, KeyPrize):
    item = StayVoucherItem
    _nickname = TreasureHunterNickname(
        nickname="Special Ticket",
        description="You can probably redeem it at a\n fancy hotel.",
    )
    remake_only = True
    _model = CardObject
    _packet_data = (SPR0206_CARD, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["StayVoucherPrize"]
