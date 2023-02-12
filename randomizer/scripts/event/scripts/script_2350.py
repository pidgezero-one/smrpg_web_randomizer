# E2350_CLIMB_GARDENER_BEANSTALK

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
                    index=7,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASTransferToXYZF(x=8, y=87, z=9, direction=EAST),
                ASSetWalkingSpeed(NORMAL),
                ASPause(4),
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$ \x00\x00\x00")),
                ASShiftZUpSteps(10),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(16), ASSetWalkingSpeed(SLOW), ASShiftNorthSteps(5)],
        ),
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
        Return(),
    ]
)
