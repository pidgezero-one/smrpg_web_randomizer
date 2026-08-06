from __future__ import annotations
from randomizer.data.items.items import (EnduringBroochItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class EnduringBroochPrize(ItemPrize):
    item = EnduringBroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    remake_only = True
    _monstro_shuffle = True
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["EnduringBroochPrize"]
