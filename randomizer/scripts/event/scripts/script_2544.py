# pylint: disable=C0301

"""E2544_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        FreezeCamera(),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2544_apply_tile_mod_10"]),
        SetBit(TEMP_7043_0),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            mod_id=0,
            identifier="EVENT_2544_apply_tile_mod_10",
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASJmpIfBitClear(
                    TEMP_7043_0,
                    ["EVENT_2544_action_queue_sync_11_SUBSCRIPT_shift_z_up_steps_4"],
                ),
                ASWalkNorthwestPixels(8),
                ASFaceSouth(),
                ASShiftZUpSteps(
                    11,
                    identifier="EVENT_2544_action_queue_sync_11_SUBSCRIPT_shift_z_up_steps_4",
                ),
                ASSetWalkingSpeed(NORMAL),
                ASClearBit(TEMP_7043_0),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthPixels(8),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSoutheastPixels(8),
                ASFaceNortheast(),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSoutheastPixels(8),
                ASFaceNortheast(),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASVisibilityOff(),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_2544_action_queue_async_16_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2544_action_queue_async_16_SUBSCRIPT_pause_1"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
                ASPause(24),
            ],
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
