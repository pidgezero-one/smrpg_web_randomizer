from __future__ import annotations
from randomizer.data.items.items import (TeamworkBandItem)
from randomizer.data.physical_objects.bosses import (SPR0212_BAND_PACKET)
from randomizer.data.physical_objects.items import (BandObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class TeamworkBandPrize(ItemPrize):
    item = TeamworkBandItem
    _nickname = TreasureHunterNickname(
        nickname="Friendship Bracelet",
        description="Maybe the real treasure is the\n friends we made along the way.",
    )
    remake_only = True
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY
    _model = BandObject
    _packet_data = (SPR0212_BAND_PACKET, 0)


__all__ = ["TeamworkBandPrize"]
