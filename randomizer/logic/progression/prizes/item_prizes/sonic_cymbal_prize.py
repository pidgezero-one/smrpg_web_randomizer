from __future__ import annotations
from randomizer.data.items.items import (SonicCymbalItem)
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (MusicObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SonicCymbalPrize(ItemPrize):
    item = SonicCymbalItem
    _nickname = TreasureHunterNickname(
        nickname="Psych Percussion",
        description="This could catch monsters\n off-guard.",
    )
    _model = MusicObject
    _packet_data = (SPR0195_FLOWER, 7)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["SonicCymbalPrize"]
