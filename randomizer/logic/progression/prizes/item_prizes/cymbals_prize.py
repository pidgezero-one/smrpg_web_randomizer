from __future__ import annotations
from randomizer.data.items.items import (CymbalsItem)
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (MusicObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class CymbalsPrize(ItemPrize):
    item = CymbalsItem
    _nickname = TreasureHunterNickname(
        nickname="Percussion Plate", description="I bet it could get pretty loud."
    )
    _model = MusicObject
    _packet_data = (SPR0195_FLOWER, 7)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["CymbalsPrize"]
