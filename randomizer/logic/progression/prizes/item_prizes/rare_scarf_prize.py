from __future__ import annotations
from randomizer.data.items.items import (RareScarfItem)
from randomizer.data.physical_objects.bosses import (SPR0212_BAND_PACKET)
from randomizer.data.physical_objects.items import (BandObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RareScarfPrize(ItemPrize):
    item = RareScarfItem
    _nickname = TreasureHunterNickname(
        nickname="White Cloth", description="You don't see these around often."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY
    _model = BandObject
    _packet_data = (SPR0212_BAND_PACKET, 0)


__all__ = ["RareScarfPrize"]
