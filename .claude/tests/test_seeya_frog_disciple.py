"""SeeYa + shop shuffle must not strand a Frog Disciple slot.

Starting with See Ya removes SeeYaPrize — Frog Disciple 1's item — from the
shuffle pool (items.py pull_prize / shuffle_rules). There are 5 Frog Disciple
locations, all must-fill (a key/frog-coin item, can't be empty), so dropping
one item leaves 5 slots for 4 items. The setup compensates by removing
FrogDiscipleLocation1 — but that removal used to be gated on shops NOT being
shuffled, so SeeYa + ShuffleShops kept all five slots and one could never be
filled, failing every seed with "FrogDiscipleLocation... is empty but cannot
be empty" out of post_shuffle_cleanup.
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smrpg_web_randomizer.settings")
django.setup()

from randomizer.main import create  # noqa: E402
from randomizer.data.shops.shops import SH03_FROG_DISCIPLE  # noqa: E402
from randomizer.data.variables.variable_names import (  # noqa: E402
    FROG_DISCIPLE_ITEM_5_PURCHASED,
)
from randomizer.logic.progression.prizelocations import FrogDiscipleLocation1  # noqa: E402
from randomizer.types.prizelocation import FrogDiscipleLocation  # noqa: E402
from randomizer.types.settings import Settings  # noqa: E402
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (  # noqa: E402
    SetBit,
)


def _frog_bit5_set(world) -> bool:
    return any(
        isinstance(c, SetBit) and c.bit == FROG_DISCIPLE_ITEM_5_PURCHASED
        for c in world.event_2496_startup
    )

# Faithful to the report, minus the prize offset (the shortage is offset-
# independent: it's the pool/location count, which the offset never touches).
BASE = (
    "P(rchars|starters:9) C(exp:double|charspells) X(rstars|proglogic:hard) "
    "A(bw:open|fm:open|bt:open|mm:open|sea:open|mt:open|bv:open|bk:open|wf:open) "
    "O(seaside:open|objective:smithy|cwarp|bwarp|skipcart|skipant) "
    "S(rshops|free) B(rboss)"
)


def _settings(flags: str) -> Settings:
    s = Settings()
    s.set_from_flag_string(flags)
    s.debug_mode = True
    return s


def test_seeya_with_shop_shuffle_generates_and_drops_frog1():
    """SeeYa + ShuffleShops: the SeeYa slot is dropped and the rest fill."""
    world = create(4171454810, _settings(BASE + " F(seeya)"))

    assert FrogDiscipleLocation1 not in world.locations
    frogs = [l for l in world.locations.values() if isinstance(l, FrogDiscipleLocation)]
    assert len(frogs) == 4
    assert all(l.has_item for l in frogs), (
        "a Frog Disciple slot is empty but cannot be empty"
    )
    # The rendered shop has exactly the four surviving items, no SeeYa, no gap.
    shop_items = [i for i in (world.shops.shops[SH03_FROG_DISCIPLE].items or []) if i]
    assert len(shop_items) == 4


def test_no_seeya_keeps_all_five_frog_disciples():
    """Control: without SeeYa the SeeYa item stays in the pool, all 5 slots exist."""
    world = create(4171454810, _settings(BASE))

    assert FrogDiscipleLocation1 in world.locations
    frogs = [l for l in world.locations.values() if isinstance(l, FrogDiscipleLocation)]
    assert len(frogs) == 5


def test_both_shuffled_keeps_five_frog_items_and_no_salebit():
    """SeeYa + shops AND items shuffled: pool surplus fills slot 5, so the shop
    keeps all 5 items and the pre-bought sale bit stays clear. Removing the slot
    here (as the first fix did) left a 4-item shop with the bit unset -> a
    glitched empty menu."""
    world = create(1200611952, _settings(BASE + " T(ritems) F(seeya)"))
    assert FrogDiscipleLocation1 in world.locations
    shop_items = [i for i in (world.shops.shops[SH03_FROG_DISCIPLE].items or []) if i]
    assert len(shop_items) == 5
    assert not _frog_bit5_set(world)


def test_items_off_reduced_shop_sets_salebit():
    """SeeYa + shops on but items off: shop shrinks to 4, so the 5th sale bit
    MUST be pre-set (else empty-slot glitch)."""
    world = create(1200611952, _settings(BASE + " F(seeya)"))
    assert FrogDiscipleLocation1 not in world.locations
    assert _frog_bit5_set(world)
