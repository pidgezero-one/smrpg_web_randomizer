"""ReplaceItems works independently of ShuffleItems.

Replacing the worst consumables (Wilt Shroom, Mushroom, ...) with coins is a
separate feature from shuffling item rewards. It used to live only in
pull_prize's shuffle branch, so with ShuffleItems off it did nothing. It now
runs at the vanilla-fill step too, gated by can_accept so coin-capable
locations (chests, most NPC/event spots) get coins while item-only spots like
StartingItem keep their item.
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smrpg_web_randomizer.settings")
django.setup()

from randomizer.main import create  # noqa: E402
from randomizer.logic.progression.prizelocations import MushroomKingdomChair  # noqa: E402
from randomizer.types.flags import ReplaceItems, ShuffleItems  # noqa: E402
from randomizer.types.prize import CoinPrize  # noqa: E402
from randomizer.types.prizelocation import TreasureChestLocation  # noqa: E402
from randomizer.types.settings import Settings  # noqa: E402

BASE = (
    "P(rchars) X(rstars) "
    "A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open) "
    "O(seaside:open|objective:smithy|cwarp|bwarp|skipcart|skipant) B(rboss)"
)


def _make(ritems: bool, replace: bool):
    s = Settings()
    s.set_from_flag_string(BASE)
    s.get_flag(ShuffleItems).enabled = ritems
    s.get_flag(ReplaceItems).enabled = replace
    return create(20260718, s)


def _chest_coins(world) -> int:
    return sum(
        1 for l in world.locations.values()
        if isinstance(l, TreasureChestLocation) and l.has_item and isinstance(l.prize, CoinPrize)
    )


def test_replace_items_with_shuffle_off_generates_and_makes_coins():
    """The previously-broken combo: no item shuffle, replace on. Must not strand."""
    baseline = _chest_coins(_make(ritems=False, replace=False))
    with_replace = _chest_coins(_make(ritems=False, replace=True))
    # ReplaceItems off leaves the vanilla worst-items in chests; on turns some to coins.
    assert with_replace > baseline, (baseline, with_replace)


def test_replace_items_reaches_npc_chair_on_reported_seed():
    """MushroomKingdomChair (an NPC/event spot) held a Mushroom; ReplaceItems -> coin."""
    s = Settings()
    s.set_from_flag_string(
        "A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open) "
        "B(rboss|noheal:all) C(exp:double|stats|charspells|spellstats|avail_spells:///3H) "
        "E(enemystats:numbers_only|attacks) F(skips|nobigbang|noko|fixinv|seeya) "
        "G(button|quiz|doorshuffle) I(replace|xpstar:bosses|sj1:1|sj2:2) "
        "O(seaside:open|objective:smithy|cwarp|bwarp|skipcart|skipant) "
        "P(rchars|allyswap|starters:9) Q(perms:random|props:random|unsafe) "
        "S(rshops|nolife|showperms|free|nosell:f) X(rstars|proglogic:hard|disperse)"
    )
    world = create(1946680577, s)
    chair = world.locations.get(MushroomKingdomChair)
    assert chair is not None and isinstance(chair.prize, CoinPrize)
