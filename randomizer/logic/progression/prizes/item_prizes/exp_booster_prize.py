from __future__ import annotations
from randomizer.data.items.items import (ExpBoosterItem)
from randomizer.data.physical_objects.bosses import (SPR0238_STATIC_FROG_COIN_SMALL)
from randomizer.data.physical_objects.items import (FrogCoinItemObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class ExpBoosterPrize(ItemPrize):
    item = ExpBoosterItem
    _nickname = TreasureHunterNickname(
        nickname="Training Device", description="This'll make you strong in no time!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY
    _model = FrogCoinItemObject
    _packet_data = (SPR0238_STATIC_FROG_COIN_SMALL, 0)


__all__ = ["ExpBoosterPrize"]
