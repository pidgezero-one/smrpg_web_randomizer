# E2315_TOWER_PARACHUTE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2315_jmp_if_bit_set_9"]),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftZUpSteps(15)]),
        ActionQueueSync(
            target=NPC_1, subscript=[ASShiftZUpSteps(11), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASShiftZUpSteps(8)]),
        ActionQueueSync(target=NPC_3, subscript=[ASShiftZUpSteps(15)]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASFixedFCoordOn(), ASShiftEastPixels(4), ASShiftZUpSteps(15)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASFixedFCoordOn(),
                ASShiftEastPixels(4),
                ASShiftSouthwestPixels(4),
                ASShiftZUpSteps(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASFixedFCoordOn(), ASShiftEastPixels(4), ASShiftZUpSteps(7)],
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASFixedFCoordOn(), ASShiftEastPixels(4), ASShiftZUpSteps(15)],
        ),
        JmpIfBitSet(
            DIRECTIONAL_7045_0,
            ["EVENT_2315_freeze_camera_12"],
            identifier="EVENT_2315_jmp_if_bit_set_9",
        ),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_2315_jmp_if_bit_clear_23"]),
        FreezeCamera(identifier="EVENT_2315_freeze_camera_12"),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthSteps(8),
                ASSetWalkingSpeed(FAST),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASShiftSouthSteps(6), ASSetWalkingSpeed(NORMAL)],
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
                ASShadowOff(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\xc0\x00`\x00")),
                ASDb(bytearray(b"%\x00\n\x80\xff")),
                ASPause(40),
                ASBPL262728(),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        StopEmbeddedActionScript(MARIO),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        StopEmbeddedActionScript(SCREEN_FOCUS),
        JmpIfBitClear(
            DIRECTIONAL_7045_0,
            ["EVENT_2315_unfreeze_camera_27"],
            identifier="EVENT_2315_jmp_if_bit_clear_23",
        ),
        Pause(24),
        UnfreezeCamera(identifier="EVENT_2315_unfreeze_camera_27"),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(DIRECTIONAL_7045_0),
        Return(),
    ]
)
