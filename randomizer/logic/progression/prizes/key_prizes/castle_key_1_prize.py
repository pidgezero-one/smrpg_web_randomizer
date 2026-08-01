from __future__ import annotations
from randomizer.data.items.items import (CastleKey1Item)
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (KeyObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class CastleKey1Prize(ItemPrize, KeyPrize):
    item = CastleKey1Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject
    _packet_data = (SPR0195_FLOWER, 2)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["CastleKey1Prize"]
