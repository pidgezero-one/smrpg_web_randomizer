from __future__ import annotations
from randomizer.data.items.items import (StarEggItem)
from randomizer.data.physical_objects.bosses import (SPR0237_EGG)
from randomizer.data.physical_objects.items import (EggObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class StarEggPrize(ItemPrize):
    item = StarEggItem
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject
    _packet_data = (SPR0237_EGG, 0)


__all__ = ["StarEggPrize"]
