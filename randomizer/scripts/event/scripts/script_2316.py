# E2316_GARDENER_EXTERIOR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASShiftEastPixels(5),
                ASShiftSouthPixels(3),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        JmpIfBitSet(TEMP_GARDENER_EXTERIOR_1, ["EVENT_2316_freeze_camera_28"]),
        JmpIfBitSet(TEMP_GARDENER_EXTERIOR_2, ["EVENT_2316_freeze_camera_6"]),
        FadeInFromBlack(sync=False),
        Return(),
        FreezeCamera(identifier="EVENT_2316_freeze_camera_6"),
        ClearBit(TEMP_GARDENER_EXTERIOR_2),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShadowOff(),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(
                    index=7, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASShiftWestPixels(4),
                ASShiftZUpSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$ \x00\x00\x00")),
                ASShiftZUpSteps(8),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(32), ASSetWalkingSpeed(VERY_SLOW), ASShiftNorthSteps(5)],
        ),
        FadeInFromBlack(sync=False),
        Pause(112),
        FadeOutToBlack(sync=False, duration=32),
        EnterArea(
            room_id=R419_LAZY_SHELL_CLOUD,
            face_direction=SOUTH,
            x=4,
            y=109,
            z=10,
            run_entrance_event=True,
        ),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=0, y=76),
                ASShiftNorthPixels(8),
                ASShiftEastPixels(17),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShiftToXYCoords(x=4, y=111),
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(8),
                ASShiftWestPixels(12),
                ASSetSpriteSequence(
                    index=7, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetPriority(2),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASShiftWestPixels(5),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        SetBit(TEMP_GARDENER_EXTERIOR_1),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$\x1c\x00\x00\x00")),
                ASShiftZUpSteps(6),
                ASBPL262728(),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(16),
                ASSetSpriteSequence(
                    index=4, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASFaceNortheast(),
                ASJumpToHeight(160),
                ASShiftNortheastSteps(2),
                ASOverwriteSolidity(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
                ASShiftNortheastPixels(8),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
        FreezeCamera(identifier="EVENT_2316_freeze_camera_28"),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShadowOff(),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASOverwriteSolidity(),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASTransferToXYZF(x=9, y=88, z=24, direction=EAST),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkToXYCoords(x=4, y=67)],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$\xe3\xff\x00\x00")),
                ASShiftZDownSteps(7),
                ASBPL262728(),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
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
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO004_JUMP, channel=4),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$@\x000\x01")),
                ASDb(bytearray(b"%\xc0\x06\x80\xff")),
                ASPause(37),
                ASBPL262728(),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(NORMAL), ASShiftSouthSteps(2)],
        ),
        UnfreezeCamera(),
        ClearBit(TEMP_GARDENER_EXTERIOR_1),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
