from __future__ import annotations
from randomizer.data.items.items import (AttackScarfItem)
from randomizer.data.physical_objects.bosses import (SPR0212_BAND_PACKET)
from randomizer.data.physical_objects.items import (BandObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, SpecialItemPrizeType, TreasureHunterNickname)


class AttackScarfPrize(ItemPrize):
    item = AttackScarfItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Starry Scarf", description="It could save your life!"
    )
    _monstro_shuffle = True
    _fortune_type: FortuneEnum = FortuneEnum.ACCESSORY
    _model = BandObject
    _packet_data = (SPR0212_BAND_PACKET, 0)


__all__ = ["AttackScarfPrize"]
