# pylint: disable=C0301

"""E0389_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_SHYSTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO000_SILENCE, channel=6),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ["EVENT_389_jmp_if_object_not_in_level_11"],
        ),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        RemoveObjectFromSpecificLevel(
            NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_389_jmp_if_object_not_in_level_11",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=25, y=27, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(
            NPC_1, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM
        ),
        PauseActionScript(NPC_2),
        ActionQueueAsync(target=NPC_2, subscript=[ASFaceNortheast()]),
        SetBit(TEMP_7049_6),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        FadeInFromBlack(sync=False),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_389_action_queue_sync_30"],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASWalkNorthwestSteps(3),
                ASWalkNorthwestPixels(8),
                ASWalkNortheastSteps(4),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASWalkNortheastPixels(8),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASFixedFCoordOff(),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASPause(30), ASFaceNorth()],
            identifier="EVENT_389_action_queue_async_22",
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASPause(30), ASFaceSouth()]),
        RemoveObjectFromSpecificLevel(
            NPC_2, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM
        ),
        Return(),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASWalkNorthwestSteps(2),
                ASWalkNortheastSteps(6),
                ASVisibilityOff(),
            ],
            identifier="EVENT_389_action_queue_sync_30",
        ),
        Jmp(["EVENT_389_action_queue_async_22"]),
    ]
)
