from __future__ import annotations
from randomizer.data.items.items import (FireShellItem)
from randomizer.data.physical_objects.bosses import (SPR0249_RED_SHELL)
from randomizer.data.physical_objects.items import (RedShellObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FireShellPrize(ItemPrize):
    item = FireShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = RedShellObject
    _packet_data = (SPR0249_RED_SHELL, 0)


__all__ = ["FireShellPrize"]
