from __future__ import annotations
from randomizer.data.enemies.enemies import (MarioDollItem)
from randomizer.data.physical_objects.bosses import (SPR0233_MARIO_DOLL)
from randomizer.data.physical_objects.items import (MarioDollObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class MarioDollPrize(ItemPrize, KeyPrize):
    item = MarioDollItem
    _nickname = TreasureHunterNickname(
        nickname="Action Figure", description="Batteries not included."
    )
    _model = MarioDollObject
    _packet_data = (SPR0233_MARIO_DOLL, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["MarioDollPrize"]
