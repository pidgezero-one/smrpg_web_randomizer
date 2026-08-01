from __future__ import annotations
from randomizer.data.items.items import (RibbitStickItem)
from randomizer.data.physical_objects.bosses import (SPR0246_STICK_PACKET)
from randomizer.data.physical_objects.items import (StickObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RibbitStickPrize(ItemPrize):
    item = RibbitStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = StickObject
    _packet_data = (SPR0246_STICK_PACKET, 0)


__all__ = ["RibbitStickPrize"]
