# E3782_BEAN_VALLEY_UPPER_CHEST_ROOM_FALL_TO_WEST_VINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
            face_direction=SOUTHWEST,
            x=13,
            y=81,
            z=27,
            z_add_half_unit=True,
        ),
        JmpToSubroutine(["EVENT_3790_jmp_if_present_in_current_level_9"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftSouthwestPixels(6),
                ASSetWalkingSpeed(NORMAL),
                ASDecZCoord1Step(),
                ASFloatingOn(),
            ],
        ),
        Pause(2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
