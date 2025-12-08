# pylint: disable=C0301

"""E0597_MINES_BOSS_ROOM_EXPLOSION_RECOIL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_6),
        MoveScriptToBackgroundThread2(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASJumpToHeight(height=64, silent=True),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_597_action_queue_async_3_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(["EVENT_597_action_queue_async_3_SUBSCRIPT_pause_6"]),
                ASFaceNortheast(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASResetProperties(),
            ]),
        ClearBit(TEMP_7044_6),
        MoveScriptToMainThread(),
        Return(),
    ]
)
