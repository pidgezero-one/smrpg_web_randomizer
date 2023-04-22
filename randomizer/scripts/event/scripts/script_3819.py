# pylint: disable=C0301

"""E3819_LANDS_END_FIRST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
        JmpIfBitSet(TEMP_7042_3, ["EVENT_3819_action_queue_sync_36"]),
        ClearBit(FLOWER_TOWER_ASCENDED),
        ClearBit(SKY_BRIDGE_TUTORIAL_BIT),
        SummonObjectToSpecificLevel(
            NPC_5, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_7, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_8, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_9, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_10, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_11, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        SummonObjectToSpecificLevel(
            NPC_12, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL
        ),
        CopyVarToVar(from_var=LAST_OVERWORLD_MARKER_ID, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 39, ["EVENT_3819_jmp_if_bit_clear_50"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 45, ["EVENT_3819_jmp_if_bit_clear_50"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASWalkNortheastPixels(8)],
            identifier="EVENT_3819_action_queue_sync_36",
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASWalkWestPixels(4)]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASWalkNortheastPixels(8),
                ASShiftZUpPixels(4),
                ASFaceSouthwest(),
            ],
        ),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_3819_run_event_as_subroutine_43"]),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        JmpIfBitClear(
            TEMP_7044_7,
            ["EVENT_3819_jmp_to_event_13"],
            identifier="EVENT_3819_run_event_as_subroutine_43",
        ),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3819_jmp_to_event_13"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3819_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3819_ret_26"]),
        RunEventAsSubroutine(E3907_LANDS_END_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3819_ret_26"),
        JmpIfBitClear(
            MELODY_BAY_SONG_3_UNLOCKED,
            ["EVENT_3819_action_queue_sync_36"],
            identifier="EVENT_3819_jmp_if_bit_clear_50",
        ),
        EnterArea(
            room_id=R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS,
            face_direction=SOUTHWEST,
            x=26,
            y=103,
            z=22,
        ),
        SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        SetBit(TEMP_7044_7),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
