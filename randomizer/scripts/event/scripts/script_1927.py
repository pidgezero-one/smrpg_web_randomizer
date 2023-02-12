# E1927_TOWER_BALCONY_JUMP_OFF

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASShiftSouthwestPixels(12),
                ASShiftSouthwestSteps(7),
                ASShiftSouthwestPixels(8),
                ASSetWalkingSpeed(FASTER),
                ASJumpToHeight(144),
                ASShiftSouthwestSteps(6),
            ],
        ),
        Pause(150),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R202_BOOSTER_TOWER_ENTRANCE,
            face_direction=SOUTHWEST,
            x=5,
            y=114,
            z=15,
        ),
        JmpToEvent(E1328_TOWER_EXTERIOR_LOADER),
        Return(),
    ]
)
