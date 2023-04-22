# pylint: disable=C0301

"""E3784_BEAN_VALLEY_2ND_VINE_ROOM_EXIT_TO_1ST_VINE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R378_BEAN_VALLEY_BEANSTALKS_AREA_01,
            face_direction=NORTHEAST,
            x=5,
            y=118,
            z=23,
            z_add_half_unit=True,
        ),
        SetBit(NOTE_DIRECTION),
        SetSyncActionScript(NPC_0, A0977_NOTE_WITHOUT_KNIFE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(8),
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
