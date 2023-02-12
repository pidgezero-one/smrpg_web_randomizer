# E3787_NIMBUS_MEZZANINE_FALL_TO_EAST_VINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02,
            face_direction=NORTHEAST,
            x=26,
            y=120,
            z=29,
        ),
        JmpToSubroutine(["EVENT_3780_jmp_if_present_in_current_level_9"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftNortheastPixels(8),
                ASSetWalkingSpeed(NORMAL),
                ASDecZCoord1Step(),
                ASFloatingOn(),
            ],
        ),
        Pause(2),
        FadeInFromBlack(sync=False),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 39),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3787_ret_6"]),
        RunEventAsSubroutine(E3911_BEAN_VALLEY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3787_ret_6"),
    ]
)
