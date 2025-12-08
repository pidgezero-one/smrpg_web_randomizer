# pylint: disable=C0301

"""E2391_BEANSTALK_FROM_INSIDE_GARDENERS_HOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFloatingOff(),
                ASShadowOff(),
                ASOverwriteSolidity(),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASSetSpriteSequence(
                    index=7, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASTransferToXYZF(x=26, y=17, z=5, direction=EAST),
                ASWalkWestPixels(4),
                ASSetWalkingSpeed(NORMAL),
                ASPause(4),
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$ \x00\x00\x00")),
                ASShiftZUpSteps(10),
                ASBPL262728(),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(16), ASSetWalkingSpeed(VERY_SLOW), ASShiftNorthSteps(5)]),
        Pause(112),
        FadeOutToBlack(sync=False, duration=32),
        SetBit(TEMP_GARDENER_EXTERIOR_2),
        EnterArea(
            room_id=R417_GARDENERS_HOUSE_OUTSIDE,
            face_direction=SOUTH,
            x=8,
            y=87,
            z=3,
            run_entrance_event=True),
        Return(),
    ]
)
