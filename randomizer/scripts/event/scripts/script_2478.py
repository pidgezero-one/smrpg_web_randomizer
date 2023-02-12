# E2478_BEAN_VALLEY_BEANSTALK_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 39),
        SummonObjectToSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_6, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_7, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_9, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_10, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASShiftNortheastPixels(5),
                ASShiftNorthPixels(5),
                ASShiftWestPixels(2),
                ASJmpIfBitClear(
                    TEMP_708C_4,
                    ["EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_8"],
                ),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
                ASReturn(),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_2478_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_8",
                ),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASShiftNortheastPixels(7),
                ASShiftEastPixels(4),
                ASShiftNorthPixels(1),
                ASShiftWestPixels(2),
                ASJmpIfBitClear(
                    TEMP_708C_4,
                    [
                        "EVENT_2478_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_9"
                    ],
                ),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
                ASReturn(),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_2478_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_9",
                ),
                ASVisibilityOff(),
            ],
        ),
        JmpIfBitClear(TEMP_708C_4, ["EVENT_2478_set_7000_to_object_coord_15"]),
        SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
        Set7000ToObjectCoord(
            object=MARIO,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2478_set_7000_to_object_coord_15",
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_2478_freeze_camera_19"]),
        FadeInFromBlack(sync=False),
        Return(),
        FreezeCamera(identifier="EVENT_2478_freeze_camera_19"),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShadowOff(),
                ASSetWalkingSpeed(FASTEST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASOverwriteSolidity(),
                ASSetSpriteSequence(
                    index=7, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASTransferToXYZF(x=27, y=27, z=24, direction=EAST),
                ASShiftEastPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=22, y=5),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$\xe3\xff\x00\x00")),
                ASShiftZDownSteps(8),
                ASBPL262728(),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(16),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASFaceSouthwest(),
                ASPlaySound(sound=SO004_JUMP, channel=4),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\x80\xfe\xb0\x00")),
                ASDb(bytearray(b"%\xc0\x06\x80\xff")),
                ASPause(37),
                ASBPL262728(),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASShiftSouthSteps(4)],
        ),
        UnfreezeCamera(),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
