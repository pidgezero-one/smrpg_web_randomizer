from __future__ import annotations
from randomizer.data.items.items import (StarGunItem)
from randomizer.data.physical_objects.bosses import (SPR0226_TINY_STAR)
from randomizer.data.physical_objects.items import (TinyStarObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class StarGunPrize(ItemPrize):
    item = StarGunItem
    _nickname = TreasureHunterNickname(
        nickname="Celestial Launcher",
        description="I bet you could do some real damage\n with this.",
    )
    _model = TinyStarObject
    _packet_data = (SPR0226_TINY_STAR, 0)
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["StarGunPrize"]
