from __future__ import annotations
from randomizer.data.items.items import (BambinoBombItem)
from randomizer.data.physical_objects.bosses import (SPR0205_MICROBOMB_PACKET)
from randomizer.data.physical_objects.items import (MicrobombObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class BambinoBombPrize(ItemPrize, KeyPrize):
    item = BambinoBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = MicrobombObject
    _packet_data = (SPR0205_MICROBOMB_PACKET, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["BambinoBombPrize"]
