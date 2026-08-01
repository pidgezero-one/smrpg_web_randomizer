"""Sunken Ship packet grants: conditional auto-terminate, everything else waits for A.

`Prize._PACKET_VARIANT_EVENTS` maps each freestanding grant to a presence-write-free copy
of itself (E4050-E4091). Those copies are reached ONLY via `Prize.packet_grant`, read ONLY
by `PacketLocationRow1` -- the six Sunken Ship puzzle prizes, `MarrymoreAltarHeadLocation`,
and (via an override) the shuffled Booster Tower Mario doll.

Historically every dialog reachable from a variant ended in `[await]` (0x00): a packet is
collected while standing on it, so the box must wait for A or the "Got a ..." message
flashes past. That is still the DEFAULT. What changed: the 5 non-3D-maze Sunken Ship
packets (`_autoterminate_packet = True`) are collected by a player running past the item and
should auto-terminate instead. They can't have their own events (the variants are shared and
the script table is full), so each variant now carries BOTH twins and picks at runtime:

    JmpIfBitClear(SHIP_PACKET_AUTOTERM_DIALOG, ["...await"])   # flag clear -> wait for A
    RunDialog(<autoterm [end]>, sync=True)                     # flag set   -> auto-close
    ...
    RunDialog(<await [await]>, sync=False, identifier="...await")

The flag is set as the first command of those 5 grants and cleared at the top of every
freestanding-grant container (E0227-E0241, in apply.py) so it never outlives one collection
-- including on grant paths with no dialog at all (star piece, coins, flower).

Invariants asserted here (each can regress silently):
  1. every reachable RunDialog's rendered flags match its dialog's terminator
     ([await] -> closable, async, no bit_6;  [end] -> sync);
  2. every dialog-bearing variant offers BOTH an [await] and an [end] twin, gated by a
     JmpIf*Bit on SHIP_PACKET_AUTOTERM_DIALOG (so the choice is actually wired);
  3. the 5 running packets set that flag as their grant's first command; the 3D maze and
     the Marrymore altar do NOT (they must keep waiting for A);
  4. the container events clear the flag before dispatching (no leak between collections);
  5. Booster Hill still auto-terminates via a path that never touches this flag or table.

Flag encoding is checked against rendered bytes, not kwargs, so a change in RunDialog's bit
layout can't quietly invalidate this.
"""

import pytest
from smrpgpatchbuilder.datatypes.dialogs.classes import DIALOG_BANK_22
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    ClearBit,
    JmpIfBitClear,
    JmpIfBitSet,
    JmpToEvent,
    RunDialog,
    SetBit,
)

from randomizer import main
from randomizer.data.variables.event_script_names import (
    E0227_FREESTANDING_15_GRANT,
    E0241_FREESTANDING_1_GRANT,
)
from randomizer.data.variables.variable_names import SHIP_PACKET_AUTOTERM_DIALOG as FLAG
from randomizer.types.gameworld import Settings
from randomizer.types.prize import Prize
from randomizer.logic.progression.prizelocations import (
    MarrymoreAltarHeadLocation,
    Ship3DMazePuzzle,
    ShipBarrelPuzzle,
    ShipCannonballPuzzle,
    ShipRatStairsBoxesLocation,
    ShipTroopaPuzzleLocation,
    ShipTrampolinePuzzle,
)
from randomizer.logic.progression.prizes import RecoveryMushroomPrize

# RunDialog.render() packs the flags into the high byte of the 16-bit dialog id arg:
#   bit 5 = closable, bit 6 = bit_6, bit 7 = (not sync)
CLOSABLE = 1 << 5
BIT_6 = 1 << 6
ASYNC = 1 << 7

# The 5 Sunken Ship packets a running player collects; auto-terminate. Everything else
# reaching these variants (3D maze, Marrymore altar, Booster Tower doll) must wait for A.
AUTOTERM_SHIP_LOCATIONS = [
    ShipBarrelPuzzle,
    ShipCannonballPuzzle,
    ShipRatStairsBoxesLocation,
    ShipTroopaPuzzleLocation,
    ShipTrampolinePuzzle,
]


def _is_flag(cmd) -> bool:
    return cmd.bit.byte == FLAG.byte and cmd.bit.bit == FLAG.bit


@pytest.fixture(scope="module")
def world():
    return main.create(seed=20260713, settings=Settings())


def _dialog_text(world, dialog_id: int) -> str:
    dialog = world.overworld_dialogs.dialogs[dialog_id]
    return world.overworld_dialogs.raw_data[dialog.bank - DIALOG_BANK_22][dialog.index]


def _reachable_commands(world, event_id: int):
    """Every command reachable from event_id, following JmpToEvent."""
    seen: set[int] = set()
    stack = [event_id]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        script = world.event_scripts.get_script_by_id(current)
        if script is None:
            continue
        for cmd in script.contents:
            yield current, cmd
            if isinstance(cmd, JmpToEvent):
                stack.append(cmd.destination)


@pytest.mark.parametrize(
    "variant_event", sorted(set(Prize._PACKET_VARIANT_EVENTS.values()))
)
def test_packet_variant_dialogs_conditional_autoterm(world, variant_event):
    dialogs = []       # (event_id, RunDialog, terminator_text)
    reads_flag = False
    for event_id, cmd in _reachable_commands(world, variant_event):
        if isinstance(cmd, (JmpIfBitClear, JmpIfBitSet)) and _is_flag(cmd):
            reads_flag = True
        elif isinstance(cmd, RunDialog):
            assert isinstance(cmd.dialog_id, int), (
                f"E{event_id}: dialog id is a var; can't resolve its terminator"
            )
            dialogs.append((event_id, cmd, _dialog_text(world, cmd.dialog_id).rstrip()))

    if not dialogs:
        # No "Got ..." box on this path (star piece / coins / flower). Nothing to gate.
        return

    awaits, ends = [], []
    for event_id, cmd, text in dialogs:
        flags = bytes(cmd.render())[2]
        where = f"E{event_id} dialog {cmd.dialog_id}"
        if text.endswith("[await]"):
            assert flags & CLOSABLE, f"{where}: [await] needs closable=True"
            assert flags & ASYNC, f"{where}: [await] needs sync=False, else the event blocks"
            assert not flags & BIT_6, f"{where}: bit_6 is the [end] convention"
            awaits.append(cmd.dialog_id)
        elif text.endswith("[end]"):
            assert not flags & ASYNC, (
                f"{where}: [end] (auto-terminate) needs sync=True so the box self-closes"
            )
            ends.append(cmd.dialog_id)
        else:
            pytest.fail(f"{where} ends in {text[-8:]!r}, not [await] or [end]")

    assert awaits, f"E{variant_event}: no [await] twin -- standing collectors need one"
    assert ends, f"E{variant_event}: no [end] twin -- running ship packets need auto-terminate"
    assert reads_flag, (
        f"E{variant_event}: dialogs present but nothing reads SHIP_PACKET_AUTOTERM_DIALOG; "
        f"the auto-terminate branch is unreachable"
    )


def test_autoterm_ship_locations_set_flag_first():
    """The 5 running packets prepend SetBit(SHIP_PACKET_AUTOTERM_DIALOG) to their grant."""
    for cls in AUTOTERM_SHIP_LOCATIONS:
        loc = cls()
        loc.set_prize(RecoveryMushroomPrize())
        first = loc.grant().contents[0]
        assert isinstance(first, SetBit) and _is_flag(first), (
            f"{cls.__name__}: grant must open with SetBit(SHIP_PACKET_AUTOTERM_DIALOG) so "
            f"the shared variant picks the auto-terminating dialog; got {first!r}"
        )


def test_waiting_packet_locations_do_not_set_flag():
    """3D maze and Marrymore altar keep waiting for A -- they must NOT set the flag."""
    for cls in (Ship3DMazePuzzle, MarrymoreAltarHeadLocation):
        loc = cls()
        loc.set_prize(RecoveryMushroomPrize())
        cmds = loc.grant().contents
        assert not any(isinstance(c, SetBit) and _is_flag(c) for c in cmds), (
            f"{cls.__name__} sets SHIP_PACKET_AUTOTERM_DIALOG but must stay [await]"
        )


def test_freestanding_grant_containers_clear_flag(world):
    """Every freestanding-grant container clears the flag before dispatch, so a set flag
    from one collection (incl. no-dialog star/coin grants) can't leak into the next."""
    for key in range(E0227_FREESTANDING_15_GRANT, E0241_FREESTANDING_1_GRANT + 1):
        script = world.event_scripts.get_script_by_id(key)
        assert script is not None and script.contents, f"E{key} missing"
        assert any(
            isinstance(c, ClearBit) and _is_flag(c) for c in script.contents
        ), f"E{key} never clears SHIP_PACKET_AUTOTERM_DIALOG -- flag can leak across collections"


def test_booster_hill_still_auto_terminates(world):
    """The inverse invariant: Booster Hill must NOT be dragged into the [await] table."""
    from randomizer.data.variables.event_script_names import E0215_HILL_ITEM

    dialogs = [
        cmd
        for _, cmd in _reachable_commands(world, E0215_HILL_ITEM)
        if isinstance(cmd, RunDialog)
    ]
    assert dialogs, "E0215_HILL_ITEM runs no dialog; test is checking the wrong event"
    awaiting = [
        cmd.dialog_id
        for cmd in dialogs
        if isinstance(cmd.dialog_id, int)
        and not _dialog_text(world, cmd.dialog_id).rstrip().endswith("[end]")
    ]
    assert not awaiting, (
        f"Booster Hill dialogs must auto-terminate (Mario is running and cannot press A); "
        f"dialogs {awaiting} do not end in [end]"
    )


def test_booster_tower_mario_doll_grant_uses_await_variants():
    """The shuffled curtain-rod prize routes through packet_grant (the [await] variants) and
    does NOT set the auto-terminate flag: it is bonked off the rod and must wait for A."""
    from randomizer.logic.progression.prizelocations import BoosterTowerMarioDollLocation
    from randomizer.logic.progression.prizes import ShoesPrize, StarPiece1

    await_targets = set(Prize._PACKET_VARIANT_EVENTS.values())
    sample_prizes = [RecoveryMushroomPrize(), StarPiece1(), ShoesPrize()]

    for prize in sample_prizes:
        if prize.standing_grant is None:
            continue
        loc = BoosterTowerMarioDollLocation()
        loc.set_prize(prize)
        cmds = loc.grant().contents
        assert not any(isinstance(c, SetBit) and _is_flag(c) for c in cmds), (
            f"{type(prize).__name__}: doll grant must not auto-terminate"
        )
        jumps = [c.destination for c in cmds if isinstance(c, JmpToEvent)]
        assert jumps, f"{type(prize).__name__}: doll grant has no JmpToEvent"
        stray = [j for j in jumps if j not in await_targets]
        assert not stray, (
            f"{type(prize).__name__}: doll grant jumps to {stray}, not an [await] packet "
            f"variant. Route it through packet_grant so the curtain-rod prize waits for A."
        )


def test_packet_variants_are_not_reachable_from_booster_hill(world):
    """Guards the premise the whole split rests on: no hill_grant enters the table."""
    variants = set(Prize._PACKET_VARIANT_EVENTS.values())
    prizes = {loc.prize for loc in world.locations.values() if loc.prize is not None}
    assert prizes, "no prizes placed; test is inspecting an empty world"

    for prize in prizes:
        hill = prize.hill_grant
        if hill is None:
            continue
        for cmd in hill.contents:
            if isinstance(cmd, JmpToEvent):
                assert cmd.destination not in variants, (
                    f"{type(prize).__name__}.hill_grant jumps into a packet variant "
                    f"(E{cmd.destination}). Booster Hill needs auto-terminating dialogs; "
                    f"the packet variants are [await] unless the ship flag is set."
                )
