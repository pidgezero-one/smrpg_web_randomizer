# pylint: disable=C0301

"""E3615_CLIMB_UP_VALLEY_BEANSTALK_INTO_VINE_CLOUDS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R378_BEAN_VALLEY_BEANSTALKS_AREA_01,
            face_direction=NORTHWEST,
            x=6,
            y=123,
            z=0,
        ),
        Db(bytearray(b"\xfdI")),
        SetBit(NOTE_DIRECTION),
        SetSyncActionScript(NPC_0, A0977_NOTE_WITHOUT_KNIFE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASWalkNorthwestSteps(2),
                ASWalkNorthwestPixels(20),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3615_pause_6"),
        JmpIfMarioInAir(["EVENT_3615_pause_6"]),
        Return(),
    ]
)
