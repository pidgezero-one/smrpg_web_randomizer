# E3779_BEAN_VALLEY_1ST_VINE_ROOM_EXIT_TO_2ND_VINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnterArea(
            room_id=R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            face_direction=NORTHWEST,
            x=7,
            y=59,
            z=0,
        ),
        Db(bytearray(b"\xfdI")),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
            ["EVENT_3779_action_queue_sync_6"],
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        ActionQueueSync(target=NPC_1, subscript=[ASShadowOff()]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASShiftNorthwestPixels(20),
                ASShiftNorthwestSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3779_action_queue_sync_6",
        ),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3779_pause_8"),
        JmpIfMarioInAir(["EVENT_3779_pause_8"]),
        Return(),
    ]
)
