# pylint: disable=C0301

"""E1855_KEEP_DONKEY_ROOM_BARREL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7043_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASPlaySound(sound=SO105_SURPRISE, channel=4),
                ASSetAllSpeeds(FAST),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=64, silent=True),
                ASFloatingOn(),
                ASWalk1StepSouth(
                    identifier="EVENT_1855_action_queue_async_1_SUBSCRIPT_walk_1_step_south_7"
                ),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
                ASJmpIfVarNotEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_1855_action_queue_async_1_SUBSCRIPT_walk_1_step_south_7"]),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=96, silent=True),
                ASPause(
                    1, identifier="EVENT_1855_action_queue_async_1_SUBSCRIPT_pause_13"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1855_action_queue_async_1_SUBSCRIPT_pause_13"]
                ),
            ]),
        Jmp(["EVENT_1830_store_coin_amount_7000_10"]),
    ]
)
