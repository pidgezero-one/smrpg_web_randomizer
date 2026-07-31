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
from randomizer.management.commands.sprite_loader_events import build_map


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


def test_load_bearing_label_edges_survive():
    """154 and 315 resolve only via a cross-script label whose identifier names a
    different script. script_3797.py shows the same shape can be decorative, so
    the edge rule must accept these two and reject that one."""
    assert ROOM_SPRITE_LOADER[154] == 790
    assert ROOM_SPRITE_LOADER[315] == 802
