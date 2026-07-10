"""Mark player-chosen items as unsellable.

Sets the ``no_sell`` bit (item stat byte 0, bit 6) on whichever items the
``ProtectSpecialItems`` flag selects. The bit is read by the
``unsellable_items`` ASM patch, which bars those items from the Sell Items
menu and from the Waste Basket.

The bit is inert on its own -- no vanilla code reads it -- so applying it is
safe regardless of which patches are active.

Debug Candy is not handled here: it carries ``_no_sell`` statically in
``items.py`` because it must always be protected and is unreachable outside
debug builds.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from ...data.items import (
    EarlierTimesItem,
    GoodieBagItem,
    LambsLureItem,
    LuckyJewelItem,
    MysteryEggItem,
    SeeYaItem,
    SheepAttackItem,
    StarEggItem,
)
from ...types.flags import ProtectedItemEnum, ProtectSpecialItems

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld

# One option can cover several items. The progressive egg chain is a single
# choice because the three items are one upgrade path (see ProgressiveEggPrize).
_PROTECTED_ITEMS: dict[ProtectedItemEnum, tuple[type, ...]] = {
    ProtectedItemEnum.LUCKY_JEWEL: (LuckyJewelItem,),
    ProtectedItemEnum.SEE_YA: (SeeYaItem,),
    ProtectedItemEnum.EARLIER_TIMES: (EarlierTimesItem,),
    ProtectedItemEnum.GOODIE_BAG: (GoodieBagItem,),
    ProtectedItemEnum.PROGRESSIVE_EGGS: (MysteryEggItem, LambsLureItem, SheepAttackItem),
    ProtectedItemEnum.STAR_EGG: (StarEggItem,),
}


def apply_item_protection(world: "GameWorld") -> None:
    """Set no_sell on every item the player chose to protect."""
    selected = world.settings.get_flag(ProtectSpecialItems).enabled
    for option in selected:
        for item_class in _PROTECTED_ITEMS[option]:
            world.get_item(item_class).set_no_sell(True)
