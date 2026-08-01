from __future__ import annotations
from randomizer.data.items.items import (SageStickItem)
from randomizer.data.physical_objects.bosses import (SPR0246_STICK_PACKET)
from randomizer.data.physical_objects.items import (StickObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SageStickPrize(ItemPrize):
    item = SageStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    remake_only = True
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = StickObject
    _packet_data = (SPR0246_STICK_PACKET, 0)


__all__ = ["SageStickPrize"]
