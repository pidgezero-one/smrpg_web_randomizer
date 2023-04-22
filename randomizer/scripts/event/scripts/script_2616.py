# pylint: disable=C0301

"""E2616_FACTORY_4TH_ROOM_GREEN_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(NPC_14),
        SetBit(UNUSED_7091_4),
        ActionQueueAsync(
            target=NPC_14,
            subscript=[
                ASPlaySound(sound=SO009_GREEN_SWITCH, channel=4),
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=7, y=82),
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASWalkSouthPixels(6),
            ],
        ),
        SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(NORMAL), ASWalkToXYCoords(x=0, y=61)],
        ),
        Pause(1, identifier="EVENT_2616_pause_6"),
        JmpIfBitSet(TEMP_7044_1, ["EVENT_2616_pause_6"]),
        SetBit(TEMP_7044_2),
        SetSyncActionScript(NPC_13, A0944_CRANE_FOR_FINAL_FACTORY_BOSS),
        Pause(1, identifier="EVENT_2616_pause_10"),
        JmpIfBitClear(TEMP_7044_3, ["EVENT_2616_pause_10"]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=3, y=66)]),
        Pause(1, identifier="EVENT_2616_pause_13"),
        JmpIfBitClear(TEMP_7044_4, ["EVENT_2616_pause_13"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(16),
                ASSetSpriteSequence(
                    index=13, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(16),
                ASSetSpriteSequence(
                    index=14, sprite_offset=2, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(32),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASDecZCoord1Step(),
                ASShiftZDownPixels(6),
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(11),
                ASSetSpriteSequence(
                    index=4, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(8),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(56),
                ASWalkWestPixels(1),
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(2),
                ASFaceNortheast(),
                ASJumpToHeight(108),
                ASPause(16),
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Pause(24),
        UnfreezeCamera(),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASShiftZUpSteps(5),
                ASPause(16),
                ASWalkNortheastSteps(4),
                ASWalkNortheastPixels(3),
                ASPause(16),
                ASWalkNorthwestSteps(9),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASOverwriteSolidity(),
                ASShiftZUpSteps(5),
                ASPause(16),
                ASWalkNortheastSteps(4),
                ASWalkNortheastPixels(3),
                ASPause(16),
                ASWalkNorthwestSteps(6),
                ASShadowOff(),
                ASWalkNorthwestSteps(3),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(NORMAL), ASWalkSouthwestSteps(3)],
        ),
        FreezeCamera(),
        Pause(16),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=13, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASPause(16),
            ],
        ),
        ActionQueueSync(
            target=NPC_13, subscript=[ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)]
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=3, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASPlaySound(sound=SO004_JUMP, channel=4),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\xd0\xfd\xb0\x01")),
                ASDb(bytearray(b"%\xc0\x06\xa0\xff")),
                ASPause(27),
                ASPlaySound(sound=SO019_LONG_FALL, channel=4),
                ASDb(bytearray(b"$@\x00\x00\x00")),
                ASPause(16),
                ASDb(bytearray(b"$\x00\x00\x00\x00")),
                ASPause(1),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASPause(1),
                ASSetPriority(1),
                ASPause(6),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(37),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x00\xd0\xff")),
                ASPause(59),
            ],
        ),
        Pause(88),
        FadeOutToBlack(sync=False, duration=8),
        Pause(48),
        JmpToEvent(E3791_OPEN_FACTORY_FINAL_BOSS_ROOM),
        Return(),
    ]
)
