# pylint: disable=C0301

"""E3192_MINES_LEFT_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        SetBit(TEMP_7043_0),
        RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3192_clear_bit_14"]),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_3192_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0",
                ),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceMario(),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(NORMAL),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASJumpToHeight(56),
                ASPause(32),
                ASPause(
                    1, identifier="EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_10"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_3192_action_queue_sync_4_SUBSCRIPT_pause_10"]
                ),
                ASPause(32),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASPause(32),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkSoutheastSteps(3),
                ASWalkSouthwestSteps(3),
                ASWalkSoutheastSteps(2),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ],
        ),
        SetBit(MINES_HENCHMAN_LEFT_DEFEATED),
        SetBit(TEMP_7043_1),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ClearBit(TEMP_7043_0, identifier="EVENT_3192_clear_bit_14"),
        Return(),
    ]
)
