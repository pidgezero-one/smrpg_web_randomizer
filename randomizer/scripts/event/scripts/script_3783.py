# E3783_BEAN_VALLEY_EAST_VINE_ROOM_EXIT_TO_2ND_VINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            face_direction=NORTHEAST,
            x=6,
            y=51,
            z=23,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            ["EVENT_3783_action_queue_sync_4"],
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        ActionQueueSync(target=NPC_1, subscript=[ASShadowOff()]),
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
            identifier="EVENT_3783_action_queue_sync_4",
        ),
        Pause(2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
