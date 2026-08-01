from __future__ import annotations
from randomizer.data.items.items import (RoyalDressItem)
from randomizer.data.physical_objects.bosses import (SPR0231_DRESS)
from randomizer.data.physical_objects.items import (DressObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RoyalDressPrize(ItemPrize):
    item = RoyalDressItem
    _nickname = TreasureHunterNickname(
        nickname="Fancy Dress", description="Check out the gold trim!"
    )
    _model = DressObject
    _packet_data = (SPR0231_DRESS, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR


__all__ = ["RoyalDressPrize"]
