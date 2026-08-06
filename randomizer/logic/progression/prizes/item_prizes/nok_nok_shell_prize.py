from __future__ import annotations
from randomizer.data.items.items import (NokNokShellItem)
from randomizer.data.physical_objects.bosses import (SPR0250_GREEN_SHELL)
from randomizer.data.physical_objects.items import (GreenShellObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class NokNokShellPrize(ItemPrize):
    item = NokNokShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = GreenShellObject
    _packet_data = (SPR0250_GREEN_SHELL, 0)


__all__ = ["NokNokShellPrize"]
