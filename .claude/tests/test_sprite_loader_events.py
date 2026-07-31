"""Each room's reserved sprite-loader stub is the injection point for palette
row bumps.

All 96 *_SHUFFLED_NPC_ANIMATION_LOADER scripts are empty and already invoked
from their room's loader -- room 315's is RunEventAsSubroutine(E0802_...) at
script_1146.py:67, inside the boss-available branch. Because they are subroutine
calls rather than tail jumps, they sidestep the E0015 fade-ordering landmine.

Naive reachability is ambiguous: traversing shared hub events returns five
candidate stubs for room 315. The generator resolves by nearest caller and raises
at build time on anything still ambiguous, so ambiguity is settled by hand once,
never at seed time.
"""
from randomizer.data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER
from randomizer.management.commands.sprite_loader_events import (
    _edges,
    _label_registries,
    _load,
    build_map,
)


def test_map_matches_regeneration():
    assert build_map() == ROOM_SPRITE_LOADER


def test_room_315_maps_to_its_own_stub():
    """E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER."""
    assert ROOM_SPRITE_LOADER[315] == 802


def test_no_stub_serves_two_rooms():
    stubs = list(ROOM_SPRITE_LOADER.values())
    assert len(stubs) == len(set(stubs))


def test_every_mapped_stub_is_empty():
    """A stub with content is not a free injection point -- appending to it
    would run alongside whatever else is there."""
    import re
    import pathlib

    for room_id, event_id in ROOM_SPRITE_LOADER.items():
        path = pathlib.Path(
            f"randomizer/data/overworld_scripts/event/scripts/script_{event_id}.py"
        )
        body = path.read_text().split("script = EventScript(", 1)[-1]
        commands = re.findall(r"\b([A-Z]\w+)\(", body)
        assert commands == ["Return"], (
            f"room {room_id} stub E{event_id:04d} is not empty: {commands}"
        )


def test_label_gate_rejects_decorative_identifiers():
    """script_3797.py carries identifier="EVENT_2064_action_queue_11", the same
    string script_2064.py uses for its own label. Trusting the embedded digit
    alone would fabricate an edge 3797 -> 2064. Trusting mere "is it referenced
    somewhere" would too: script_2064.py's own JmpIfBitSet(...) does reference
    it, so only the uniqueness check (the string is defined in both 2064 and
    3797) rejects it. Exercising _edges directly, rather than the finished map,
    means this fails if either AND leg of the gate is weakened -- unlike
    asserting on ROOM_SPRITE_LOADER values, which the pre-hardening generator
    also produced."""
    name_to_id, stub_ids, scripts = _load()
    defined_in, referenced = _label_registries(scripts)
    assert 2064 not in _edges(3797, name_to_id, scripts, defined_in, referenced)
    assert 1146 in _edges(1145, name_to_id, scripts, defined_in, referenced)
    assert 3809 in _edges(3930, name_to_id, scripts, defined_in, referenced)


def test_label_dependent_rooms_still_resolve():
    """154 and 315 resolve only via a cross-script label whose identifier names
    a different script (see test_label_gate_rejects_decorative_identifiers for
    the test that exercises the gate itself). A canary against over-tightening
    the gate in a way that drops a genuine edge -- not a guard against the
    false-edge regression the gate exists for, since the pre-hardening
    generator produced these exact same values too."""
    assert ROOM_SPRITE_LOADER[154] == 790
    assert ROOM_SPRITE_LOADER[315] == 802
