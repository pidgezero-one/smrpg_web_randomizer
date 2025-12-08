# pylint: disable=C0301

"""E3717_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_FAN_GUST_PATH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_3584_ret_0"]),
        JmpIfBitClear(TEMP_7043_6, ["EVENT_3584_ret_0"]),
        FreezeAllNPCsUntilReturn(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkToXYCoords(x=15, y=112),
                ASSetSpriteSequence(
                    index=2, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSoutheastPixels(2),
                ASStartLoopNTimes(3),
                ASWalkNorthwestPixels(4),
                ASWalkSoutheastPixels(4),
                ASEndLoop(),
                ASWalkNorthwestPixels(2),
            ]),
        Pause(30),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3717_action_queue_async_6_SUBSCRIPT_pause_1"]
                ),
                ASFaceNorthwest(),
                ASResetProperties(),
                ASPause(10),
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(2),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(4),
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(2),
                ASResetProperties(),
                ASPause(2),
                ASSetSpriteSequence(
                    index=15,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(2),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(60),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Pause(10),
        UnfreezeAllNPCs(),
        ClearBit(TEMP_7043_6),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        ClearBit(TEMP_7043_6),
        Return(),
    ]
)
