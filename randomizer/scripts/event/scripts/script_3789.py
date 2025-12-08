# pylint: disable=C0301

"""E3789_BEAN_VALLEY_WEST_VINE_ROOM_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            face_direction=SOUTHWEST,
            x=3,
            y=58,
            z=26),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            ["EVENT_3789_action_queue_sync_4"]),
        RemoveObjectFromCurrentLevel(NPC_2),
        ActionQueueSync(target=NPC_1, subscript=[ASShadowOff()]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthwestPixels(6),
                ASSetWalkingSpeed(NORMAL),
                ASDecZCoord1Step(),
                ASFloatingOn(),
            ],
            identifier="EVENT_3789_action_queue_sync_4"),
        Pause(2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
