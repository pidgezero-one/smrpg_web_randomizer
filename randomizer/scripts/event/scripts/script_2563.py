# pylint: disable=C0301

"""E2563_REVEAL_BEAN_VALLEY_BEANSTALK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_708C_4, ["EVENT_2563_freeze_camera_29"]),
        SetBit(TEMP_708C_4),
        SetBit(UNKNOWN_BEANSTALK_707F_1),
        PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
        FreezeCamera(),
        Pause(32),
        ActionQueueAsync(
            target=MARIO, subscript=[ASWalkToXYCoords(x=26, y=29), ASFaceNortheast()]
        ),
        Pause(80),
        PlaySound(sound=SO127_LIGHT_RATTLE, channel=6),
        SummonObjectToCurrentLevel(NPC_0),
        SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
        PlaySound(sound=SO128_FLOATING_HOVERING, channel=6),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(64),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASShiftNorthSteps(6)]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(16),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
            ]),
        Pause(40),
        SummonObjectToCurrentLevel(NPC_1),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(64),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        Pause(8),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Pause(48),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftSouthSteps(7)]),
        Pause(16),
        ActionQueueSync(target=MARIO, subscript=[ASPause(56), ASResetProperties()]),
        StopEmbeddedActionScript(MARIO),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Jmp(["EVENT_2563_ret_38"]),
        FreezeCamera(identifier="EVENT_2563_freeze_camera_29"),
        ActionQueueSync(target=NPC_0, subscript=[ASSetVRAMPriority(NORMAL_PRIORITY)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetVRAMPriority(NORMAL_PRIORITY)]),
        ActionQueueSync(
            target=NPC_2, subscript=[ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASWalkToXYCoords(x=26, y=30),
                ASFaceNortheast(),
                ASPause(16),
                ASSetSpriteSequence(
                    index=0, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASPause(24),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASOverwriteSolidity(),
                ASFloatingOff(),
                ASPlaySound(sound=SO004_JUMP, channel=4),
                ASShadowOff(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\x80\x01\x80\x01")),
                ASDb(bytearray(b"%\x00\x0c\x80\xff")),
                ASPause(31),
                ASBPL262728(),
                ASShadowOff(),
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True),
                ASPause(24),
            ]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASShiftNorthSteps(6)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=7, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$ \x00\x00\x00")),
                ASShiftNorthSteps(10),
                ASBPL262728(),
            ]),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3615_CLIMB_UP_VALLEY_BEANSTALK_INTO_VINE_CLOUDS),
        Return(identifier="EVENT_2563_ret_38"),
    ]
)
