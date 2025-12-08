# pylint: disable=C0301

"""E3194_MINES_CENTER_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        SetBit(TEMP_7043_0),
        RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3194_clear_bit_14"]),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPause(
                    32, identifier="EVENT_3194_action_queue_sync_4_SUBSCRIPT_pause_0"
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
                    1, identifier="EVENT_3194_action_queue_sync_4_SUBSCRIPT_pause_10"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_3194_action_queue_sync_4_SUBSCRIPT_pause_10"]
                ),
                ASPause(32),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkSoutheastSteps(4),
                ASWalkNortheastSteps(3),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ]),
        SetBit(MINES_HENCHMAN_MIDDLE_DEFEATED),
        SetBit(TEMP_7043_1),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ClearBit(TEMP_7043_0, identifier="EVENT_3194_clear_bit_14"),
        Return(),
    ]
)
