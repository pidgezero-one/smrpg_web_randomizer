# pylint: disable=C0301

"""E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(60, identifier="EVENT_557_pause_0"),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=3
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=1
        ),
        SetSyncActionScript(NPC_5, A0662_ROSE_TOWN_LIBERATED_WATER_GUY),
        SetBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
        Pause(1, identifier="EVENT_557_pause_5"),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_557_set_action_script_sync_8"]),
        Jmp(["EVENT_557_pause_5"]),
        SetSyncActionScript(
            NPC_2,
            A0672_ROSE_TOWN_LIBERATED_WATER_KID,
            identifier="EVENT_557_set_action_script_sync_8"),
        SetSyncActionScript(NPC_3, A0674_ROSE_TOWN_LIBERATED_WATER_KID),
        SetSyncActionScript(NPC_4, A0675_ROSE_TOWN_LIBERATED_WATER_KID),
        Pause(1, identifier="EVENT_557_pause_11"),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_557_set_action_script_sync_14"]),
        Jmp(["EVENT_557_pause_11"]),
        SetSyncActionScript(
            NPC_5,
            A0663_ROSE_TOWN_LIBERATED_WATER_GUY,
            identifier="EVENT_557_set_action_script_sync_14"),
        Pause(1, identifier="EVENT_557_pause_15"),
        JmpIfBitSet(TEMP_7044_1, ["EVENT_557_apply_tile_mod_18"]),
        Jmp(["EVENT_557_pause_15"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R084_ROSE_TOWN_OUTSIDE,
            mod_id=2,
            identifier="EVENT_557_apply_tile_mod_18"),
        ApplySolidityModToLevel(
            permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=3
        ),
        ClearBit(TEMP_7043_7),
        ClearBit(TEMP_7044_0),
        ClearBit(TEMP_7044_1),
        ClearBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
        Pause(120),
        Jmp(["EVENT_557_pause_0"]),
    ]
)
