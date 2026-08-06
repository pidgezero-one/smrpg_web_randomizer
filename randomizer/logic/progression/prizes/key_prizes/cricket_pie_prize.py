from __future__ import annotations
from randomizer.data.items.items import (CricketPieItem)
from randomizer.data.physical_objects.bosses import (SPR0254_YOSHI_COOKIE)
from randomizer.data.physical_objects.items import (CookieObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class CricketPiePrize(ItemPrize, KeyPrize):
    item = CricketPieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject
    _packet_data = (SPR0254_YOSHI_COOKIE, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["CricketPiePrize"]
