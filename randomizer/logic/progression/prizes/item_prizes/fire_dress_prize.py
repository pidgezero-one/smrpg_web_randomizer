from __future__ import annotations
from randomizer.data.items.items import (FireDressItem)
from randomizer.data.physical_objects.bosses import (SPR0231_DRESS)
from randomizer.data.physical_objects.items import (DressObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FireDressPrize(ItemPrize):
    item = FireDressItem
    _nickname = TreasureHunterNickname(
        nickname="Red Dress", description="The pattern on it is pretty cool."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = DressObject
    _packet_data = (SPR0231_DRESS, 0)


__all__ = ["FireDressPrize"]
