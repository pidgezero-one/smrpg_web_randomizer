# pylint: disable=C0301

"""E0430_PIPE_VAULT_MARIO_HIT_BY_THWOMP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7043_3),
        JmpIfBitClear(TEMP_7043_4, ["EVENT_256_ret_0"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASShadowOff(),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASPause(
                    1, identifier="EVENT_430_action_queue_async_2_SUBSCRIPT_pause_3"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_4,
                    ["EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6"],
                ),
                ASJmp(["EVENT_430_action_queue_async_2_SUBSCRIPT_pause_3"]),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_430_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6",
                ),
                ASTransferToXYZF(x=25, y=28, z=10, direction=EAST),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkSouthwestPixels(14),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASStartLoopNTimes(3),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASTransferXYZFPixels(x=0, y=0, z=19, direction=NORTHEAST),
                ASShiftZDownPixels(3),
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASWalkSouthwestPixels(16),
                ASEndLoop(),
                ASPause(60),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOn(),
                ASSetWalkingSpeed(NORMAL),
                ASShadowOn(),
            ],
        ),
        FreezeAllNPCsUntilReturn(),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        UnfreezeAllNPCs(),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
