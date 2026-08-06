"""Collapse two differently-based NPCs in a room onto one shared sprite id.

NOT CURRENTLY WIRED INTO apply_shuffler_results. Kept as working scaffolding for
the next room that genuinely runs out of VRAM with multi-base sprites; room 315
no longer needs it. To use it, call ``merge_axem_seaside_sprites(world)``
immediately before ``update_changed_room_partitions``.

## What it does

SPR0847 carries Axem Red's standing sequence as sequence 0 and Axem Black's as
sequence 1, built by copying molds verbatim from 466/485 (both gridplane format
3, so no recompositing). This swaps room 315's Red and Black objects onto that
one sprite and queues a command telling the Black ones to show Black's art.

## Why room 315 does not use it

Two cheaper fixes removed the need:

* ``CULEX_SMALL_NPC`` and ``AXEM_RED_NPC_2_LOW_VRAM`` authored
  ``min_vram_size=1`` on gridplane sprites, costing 8 dedicated slots each where
  4 would do. Gridplane sprites live in a fixed-size block --
  ``_size_dedicated_min_vram`` early-returns on them -- so only a room's
  ``npc_expected_animations`` should ever raise it, and room 315 declares none.
  That alone was the whole VRAM overrun: it took the dedicated cursor from $44
  (past clone buffer A at $40, so object 8 overwrote object 0) down to $30.
* SPAL255 (Axem Red) and SPAL259 (Axem Black) hold byte-identical colours, so
  ``sprite_485`` simply points at Red's palette id. One CGRAM row instead of
  two, which is what frees the row the ship boss's crystal palette bump needs.

## The catch that makes this a last resort

The engine picks an animation sequence from the NPC's facing direction, and the
common directions alias to sequence 0. So the moment a script tells a merged
object to face or walk, it reverts to sequence 0 -- Axem Red -- and the borrowed
sequence is lost. Observed in room 315 via script 1147 ("face southwest",
"walk 2 steps southeast"). Loading the art as a static mold
(``is_mold=True``) is the obvious next thing to try; whether a direction change
also clobbers a mold is UNVERIFIED.

Prefer, in order: fix bogus ``min_vram_size``; share a palette id when the
colours are identical; only then reach for a shared sprite.
"""

from __future__ import annotations

from copy import copy
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_SetSpriteSequence,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    AREAOBJECT_FROM_NPC_ID as AREA_OBJECTS,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    ActionQueueSync,
)

from randomizer.data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER
from randomizer.data.variables.room_names import (
    R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
)
from randomizer.data.variables.sprite_names import (
    SPR0466_AXEM_RED,
    SPR0485_AXEM_BLACK,
    SPR0847_AXEM_RED_AND_BLACK_SHARED,
)
from randomizer.logic.progression.prizelocations import SeasideBeachBossFight
from randomizer.logic.progression.prizes import AxemRangersBossFight

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
    from randomizer.types.npc import NPC

# Sequence layout of SPR0847. Red is sequence 0 so an object that never receives
# its queued command still renders as Red rather than garbage.
_RED_SEQUENCE = 0
_BLACK_SEQUENCE = 1
# Black's art also exists as a standalone mold, for the is_mold experiment above.
_BLACK_MOLD = 2


def _record_on_sprite(npc: NPC, sprite_id: int) -> NPC:
    """A copy of ``npc`` pointing at ``sprite_id``.

    Copy, never mutate: NPC records are shared between every object referencing
    them, so writing the id in place would drag unrelated objects along.
    """
    swapped = copy(npc)
    swapped.set_sprite_id(sprite_id)
    return swapped


def merge_axem_seaside_sprites(world: GameWorld) -> None:
    """Collapse room 315's Axem Red and Black onto SPR0847."""
    location = world.locations.get(SeasideBeachBossFight)
    if location is None or not isinstance(location.prize, AxemRangersBossFight):
        return

    room = world.rooms._rooms[R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    if room is None:
        return

    black_indices: list[int] = []
    merged_any = False
    for index, obj in enumerate(room.objects):
        sprite_id = int(obj._npc.sprite_id)
        if sprite_id not in (SPR0466_AXEM_RED, SPR0485_AXEM_BLACK):
            continue
        if sprite_id == SPR0485_AXEM_BLACK:
            black_indices.append(index)
        room.objects[index]._npc = _record_on_sprite(
            obj._npc, SPR0847_AXEM_RED_AND_BLACK_SHARED
        )
        merged_any = True

    if not merged_any or not black_indices:
        return

    # Every merged object defaults to sequence 0 (Red), so the Black ones need
    # telling. The stub is an empty loader the room already invokes, so the
    # queue runs before the fade -- the same delivery path the palette row bumps
    # use.
    stub_id = ROOM_SPRITE_LOADER.get(R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH)
    if stub_id is None:
        return
    script = world.get_event_script(stub_id)
    for index in black_indices:
        script.insert_before_nth_command(
            0,
            ActionQueueSync(
                target=AREA_OBJECTS[index],
                subscript=[A_SetSpriteSequence(_BLACK_SEQUENCE, looping=True)],
            ),
        )
