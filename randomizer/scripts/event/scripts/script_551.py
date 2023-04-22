# pylint: disable=C0301

"""E0551_ROSE_TOWN_OCCUPIED_MODS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(120),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1
        ),
        SetSyncActionScript(NPC_5, A0664_ROSE_TOWN_OCCUPIED_WATER_GUY),
        Pause(60),
        ApplyTileModToLevel(
            use_alternate=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3
        ),
        Pause(1, identifier="EVENT_551_pause_7"),
        JmpIfBitClear(
            ROSE_TOWN_WATER_PUMPERS_POSITION, ["EVENT_551_apply_tile_mod_10"]
        ),
        Jmp(["EVENT_551_pause_7"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
            mod_id=3,
            identifier="EVENT_551_apply_tile_mod_10",
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1
        ),
        Pause(60),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3
        ),
        Pause(120),
        JmpToEvent(E0551_ROSE_TOWN_OCCUPIED_MODS),
    ]
)
