from __future__ import annotations
from randomizer.data.items.items import (SafetyBadgeItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SafetyBadgePrize(ItemPrize):
    item = SafetyBadgeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Button",
        description="I don't really follow politics, but\n this button looks like it's against\n a lot of things.",
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY


__all__ = ["SafetyBadgePrize"]
