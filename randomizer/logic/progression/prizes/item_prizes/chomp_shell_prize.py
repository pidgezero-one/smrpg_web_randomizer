from __future__ import annotations
from randomizer.data.items.items import (ChompShellItem)
from randomizer.data.physical_objects.bosses import (SPR0245_CHOMP_BALL)
from randomizer.data.physical_objects.items import (ChompObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class ChompShellPrize(ItemPrize):
    item = ChompShellItem
    _nickname = TreasureHunterNickname(
        nickname="Chomp Exoskeleton",
        description="I didn't even know those things\n could shed their skin.",
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = ChompObject
    _packet_data = (SPR0245_CHOMP_BALL, 0)


__all__ = ["ChompShellPrize"]
