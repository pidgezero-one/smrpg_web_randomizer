"""Read-only queries over world state.

Extracted from types/gameworld.py.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from randomizer.data.items.items import (
    AttackScarfItem,
    ChompItem,
    EnduringBroochItem,
    FroggieStickItem,
    GhostMedalItem,
    JinxBeltItem,
    LazyShellItem,
    LazyShellItem2,
    QuartzCharmItem,
    SageStickItem,
    Stella023Item,
    SuperSuitItem,
    TeamworkBandItem,
    WonderChompItem,
    ZoomShoesItem,
)
from randomizer.logic.progression.prizelocations.invisible_flags import (
    ThreeMustyFearsBonesProxy,
    ThreeMustyFearsBooProxy,
    ThreeMustyFearsGreaperProxy,
)
from randomizer.types.check_flags import (EnabledBossChecks, EnabledRegularChecks, ShuffledBosses)
from randomizer.types.prizelocation import (
    BossFightLocation,
    CharacterRecruitmentLocation,
    InvisibleFlagLocation,
    PrizeLocation,
    SpellSlotLocation,
    StarPieceLocation,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (TOTAL_FORMATIONS)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def is_monstro_item(item_type: type) -> bool:
    """Check if an item type is a special Monstro Town item."""
    return item_type in (
        ChompItem,
        ZoomShoesItem,
        FroggieStickItem,
        LazyShellItem,
        LazyShellItem2,
        GhostMedalItem,
        JinxBeltItem,
        QuartzCharmItem,
        AttackScarfItem,
        SuperSuitItem,
        WonderChompItem,
        Stella023Item,
        SageStickItem,
        EnduringBroochItem,
        TeamworkBandItem,
    )


def is_location_enabled(world: GameWorld, location_type: type[PrizeLocation]) -> bool:
    """Check if a location type is enabled based on its category flag.

    Returns True if the location is enabled in the relevant flag based on its type:
    - BossFightLocation subclasses check ShuffledBosses
    - StarPieceLocation subclasses check EnabledBossChecks
    - SpellSlotLocation subclasses are always enabled (controlled by CharacterLearnedSpells/SpellsAnywhere)
    - CharacterRecruitmentLocation subclasses are always enabled (controlled by ShuffleCharacters)
    - Other PrizeLocation subclasses check EnabledRegularChecks
    """
    if issubclass(location_type, BossFightLocation):
        # BossFightLocations check ShuffledBosses (which bosses are in the shuffle pool)
        # .enabled contains enum members, so we compare against .value
        shuffled_bosses_flag = world.settings.get_flag(ShuffledBosses)
        return any(m.value == location_type for m in shuffled_bosses_flag.enabled)
    elif issubclass(location_type, SpellSlotLocation):
        # SpellSlotLocations are always considered "enabled" here - their actual
        # shuffle status is controlled by CharacterLearnedSpells/SpellsAnywhere flags
        return True
    elif issubclass(location_type, StarPieceLocation):
        # StarPieceLocations check EnabledBossChecks (star pieces are tied to boss fights)
        boss_checks_flag = world.settings.get_flag(EnabledBossChecks)
        return any(m.value == location_type for m in boss_checks_flag.enabled)
    elif issubclass(location_type, CharacterRecruitmentLocation):
        # CharacterRecruitmentLocations are always considered "enabled" here - their actual
        # shuffle status is controlled by ShuffleCharacters flag
        return True
    elif issubclass(location_type, InvisibleFlagLocation):
        # InvisibleFlagLocations are randomly assigned to one of 3 slots at runtime.
        # Look up this class in the world's invisible item locations to find its _which value,
        # then check if the corresponding proxy is enabled.
        if world._invisible_item_locations is None:
            return False
        location_instance = world._invisible_item_locations.get(location_type)
        if not isinstance(location_instance, InvisibleFlagLocation):
            return False
        which = location_instance._which
        # Slot->fear must match the found-bit/item/hint order: i=0,1,2 set
        # flag1,2,3, which script_2081 fixes as Greaper, Big Boo, Dry Bones.
        proxy_classes = {
            0: ThreeMustyFearsGreaperProxy,
            1: ThreeMustyFearsBooProxy,
            2: ThreeMustyFearsBonesProxy,
        }
        proxy_class = proxy_classes.get(which)
        if proxy_class is None:
            return False
        regular_checks_flag = world.settings.get_flag(EnabledRegularChecks)
        return any(m.value == proxy_class for m in regular_checks_flag.enabled)
    else:
        # Check EnabledRegularChecks for non-boss locations
        regular_checks_flag = world.settings.get_flag(EnabledRegularChecks)
        return any(m.value == location_type for m in regular_checks_flag.enabled)


def allocate_formation_id(world: GameWorld) -> int:
    """Allocate a unique formation ID for a new Formation object.

    Raises:
        ValueError: If all 512 formation IDs have been exhausted.
    """

    if world._next_formation_id is None:
        max_id = 0
        for pack in world.battle_packs.packs:
            for f in pack.formations:
                if f.formation_id is not None and f.formation_id > max_id:
                    max_id = f.formation_id
        world._next_formation_id = max_id + 1
    if world._next_formation_id >= TOTAL_FORMATIONS:
        raise ValueError(
            f"Cannot allocate formation ID: all {TOTAL_FORMATIONS} slots exhausted"
        )
    fid = world._next_formation_id
    world._next_formation_id += 1
    return fid


__all__ = ['is_monstro_item', 'is_location_enabled', 'allocate_formation_id']
