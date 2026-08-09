"""Static list of every prize location check, for the "List of Checks" resource page.

Generated from the prize location classes themselves, the same way the options page
is generated from the flag classes - nothing is listed by hand, so a new location
file shows up on the page as soon as it exists.

Every PrizeLocation subclass in the prizelocations package is included, except the
two families listed in EXCLUDED_FAMILIES below. Settings are deliberately not
consulted: this is every check in the game, not the subset a seed turns on.
"""

from __future__ import annotations

import inspect
from typing import NamedTuple

from randomizer.logic.progression import prizelocations as _prizelocations_module
from randomizer.types.prize import CoinPrize, Prize
from randomizer.types.prizelocation import (
    BossFightLocation,
    CharacterRecruitmentLocation,
    InvisibleFlagLocation,
    KeyItemLocation,
    PrizeLocation,
    ShuffleLocationSelector,
    SpellSlotLocation,
    StandingLocation,
    StarPieceLocation,
    StartingCharacterLocation,
    WorldAreaEnum,
)


class CheckRow(NamedTuple):
    # Enum member name, not its value: this is the checkbox's localStorage identity,
    # so it has to survive edits to the UI-facing string.
    key: str
    world_area: str
    name: str
    check_type: str
    conditions: str


# First match wins, so keep this most-specific-first if any of these families ever
# gains a subclass of another. KeyItemLocation goes last because it is the broadest -
# it is the "can hold a key item" marker, which a fight or recruitment slot could
# also carry. Anything unmatched is an ordinary item of some kind: chest,
# freestanding pickup, shop purchase, NPC reward, river item, frog disciple.
CHECK_TYPES: tuple[tuple[type[PrizeLocation], str], ...] = (
    (BossFightLocation, "Boss fight"),
    (StarPieceLocation, "Star Piece"),
    (CharacterRecruitmentLocation, "Character"),
    (KeyItemLocation, "Key Item"),
)
DEFAULT_CHECK_TYPE = "Item"


# None of these is a check you go and find in the world:
# - InvisibleFlagLocation subclasses are the ~100 candidate hiding spots, of which a
#   seed uses exactly three. The three that get used are listed instead, via the
#   Three Musty Fears proxies below.
# - SpellSlotLocation subclasses are level-up spell slots, not world locations.
# - StartingCharacterLocation subclasses are the party you begin the game with.
EXCLUDED_FAMILIES: tuple[type[PrizeLocation], ...] = (
    InvisibleFlagLocation,
    SpellSlotLocation,
    StartingCharacterLocation,
)

# The starting inventory, likewise not something you go and find. Listed by selector
# because the four classes share no base - they're plain NPCLocationRow2..5.
EXCLUDED_SELECTORS: frozenset[ShuffleLocationSelector] = frozenset({
    ShuffleLocationSelector.MARIOS_PAD_STARTER_1,
    ShuffleLocationSelector.MARIOS_PAD_STARTER_2,
    ShuffleLocationSelector.MARIOS_PAD_STARTER_3,
    ShuffleLocationSelector.MARIOS_PAD_STARTER_4,
})

# Everything downstream of a mimic chest: the fight, its Star Piece, and its rewards.
# The _world_area on these classes is only where vanilla put the mimic - the mimic
# offset and MimicsAnywhere settings can move it into any eligible chest room, so
# stating an area would be wrong more often than right. The rows stay, the area goes.
# Listed by selector because the ten classes share no base: only the three fights are
# MimicFightLocation, the rewards are plain NPC / treasure chest rows.
MIMIC_SELECTORS: frozenset[ShuffleLocationSelector] = frozenset({
    ShuffleLocationSelector.PANDORITE_BOSS_FIGHT,
    ShuffleLocationSelector.PANDORITE_BOSS,
    ShuffleLocationSelector.PANDORITE_REWARD_1,
    ShuffleLocationSelector.PANDORITE_REWARD_2,
    ShuffleLocationSelector.HIDON_BOSS_FIGHT,
    ShuffleLocationSelector.HIDON_BOSS,
    ShuffleLocationSelector.HIDON_REWARD_1,
    ShuffleLocationSelector.HIDON_REWARD_2,
    ShuffleLocationSelector.BOX_BOY_BOSS_FIGHT,
    ShuffleLocationSelector.BOX_BOY_BOSS,
})

# The Three Musty Fears proxies are bare classes with no rooms, no _world_area and no
# type, so their whole row is written out here. They stand for the three invisible
# items a seed places, drawn from the whole InvisibleFlagLocation pool, so they're
# named as generic slots - the hiding spot is different every seed. Type is Key Item
# because what they stand for is an InvisibleFlagLocation, which is a KeyItemLocation.
#
# ORDER IS LOAD-BEARING, and it is not the enum's. prize_locations.py fills slot i
# from invisible_item_pool[i] when the flag is off, and hands slot i to a fixed ghost:
# i=0 Greaper / MariosPadBedFlag, i=1 Big Boo / RoseTownSignFlag, i=2 Dry Bones /
# YosterIsleGoalFlag. Reordering these three puts each note on the wrong row.
PROXY_ROWS: dict[ShuffleLocationSelector, tuple[str, str, str]] = {
    ShuffleLocationSelector.THREE_MUSTY_FEARS_GREAPER: (
        "Invisible item 1",
        "Key Item",
        'Stays in Mario\'s Pad if "Move invisible flag checks" is disabled',
    ),
    ShuffleLocationSelector.THREE_MUSTY_FEARS_BOO: (
        "Invisible item 2",
        "Key Item",
        'Stays in Rose Town if "Move invisible flag checks" is disabled',
    ),
    ShuffleLocationSelector.THREE_MUSTY_FEARS_BONES: (
        "Invisible item 3",
        "Key Item",
        'Stays in Yo\'ster Isle if "Move invisible flag checks" is disabled',
    ),
}

# Checks with no fixed place in the world: they render a blank Area, and they're
# listed first because they have no slot in the play-order walkthrough the rest of
# the table follows.
LOCATIONLESS_SELECTORS: frozenset[ShuffleLocationSelector] = MIMIC_SELECTORS | frozenset(
    PROXY_ROWS
)


def _selector_of(cls: type[PrizeLocation]) -> ShuffleLocationSelector | None:
    """Return the class's _id, or None if it never sets one.

    PrizeLocation declares _id as a bare annotation, so the attribute genuinely does
    not exist on classes that skip it. Walking __dict__ up the MRO reports that
    absence without an exception.
    """
    for klass in cls.__mro__:
        value = klass.__dict__.get("_id")
        if isinstance(value, ShuffleLocationSelector):
            return value
    return None


def _world_area_of(cls: type[PrizeLocation]) -> WorldAreaEnum | None:
    """Return the class's _world_area, or None if it never sets one."""
    for klass in cls.__mro__:
        value = klass.__dict__.get("_world_area")
        if isinstance(value, WorldAreaEnum):
            return value
    return None


def _check_type_of(cls: type[PrizeLocation]) -> str:
    """Return the display label for what kind of check this is."""
    for family, label in CHECK_TYPES:
        if issubclass(cls, family):
            return label
    return DEFAULT_CHECK_TYPE


def _originally_held_of(cls: type[PrizeLocation]) -> type[Prize] | None:
    """Return the class's _originally_held, or None if it never sets one."""
    for klass in cls.__mro__:
        value = klass.__dict__.get("_originally_held")
        if isinstance(value, type) and issubclass(value, Prize):
            return value
    return None


# --- TEMPORARY EXCLUSION -----------------------------------------------------
# Vanilla regular-coin pickups are hidden from the page for now. To put them back,
# delete this function and its one call in _build_rows (marked with the same
# banner), plus the CoinPrize / StandingLocation imports. Nothing else refers to it.
def _is_vanilla_coin_pickup(cls: type[PrizeLocation]) -> bool:
    """True for a freestanding pickup that vanilla filled with plain coins.

    FrogCoinPrize is a sibling of CoinPrize rather than a subclass, so freestanding
    frog coins survive this check without needing to be special cased.
    """
    if not issubclass(cls, StandingLocation):
        return False
    originally_held = _originally_held_of(cls)
    return originally_held is not None and issubclass(originally_held, CoinPrize)
# --- end temporary exclusion -------------------------------------------------


def _build_rows() -> list[CheckRow]:
    package = _prizelocations_module.__name__
    found: dict[ShuffleLocationSelector, CheckRow] = {}

    for _, cls in inspect.getmembers(_prizelocations_module, inspect.isclass):
        if cls is PrizeLocation or not issubclass(cls, PrizeLocation):
            continue
        # Abstract row bases re-exported from types.prizelocation live in another
        # package and are not concrete checks.
        if cls.__module__ != package and not cls.__module__.startswith(package + "."):
            continue
        if issubclass(cls, EXCLUDED_FAMILIES):
            continue
        # --- TEMPORARY EXCLUSION: delete this branch to list regular coins again.
        if _is_vanilla_coin_pickup(cls):
            continue
        # --- end temporary exclusion
        selector = _selector_of(cls)
        if selector is None or selector in EXCLUDED_SELECTORS:
            continue

        proxy = PROXY_ROWS.get(selector)
        if proxy is not None:
            name, check_type, conditions = proxy
        else:
            name = selector.value
            check_type = _check_type_of(cls)
            conditions = cls._access_conditions

        if selector in LOCATIONLESS_SELECTORS:
            area_label = ""
        else:
            area = _world_area_of(cls)
            if area is None:
                continue
            area_label = area.value

        found.setdefault(
            selector,
            CheckRow(selector.name, area_label, name, check_type, conditions),
        )

    # Locationless checks lead, mimics then invisible items. Everything after them is
    # in ShuffleLocationSelector order, which is authored in play order - the mimic
    # block keeps that order too, but the invisible items follow PROXY_ROWS instead
    # because their slot numbering is not the enum's.
    order = [selector for selector in ShuffleLocationSelector if selector in MIMIC_SELECTORS]
    order += PROXY_ROWS
    order += [
        selector
        for selector in ShuffleLocationSelector
        if selector not in LOCATIONLESS_SELECTORS
    ]
    return [found[selector] for selector in order if selector in found]


CHECK_ROWS: list[CheckRow] = _build_rows()
