# pylint: disable=C0301

"""E3859_WORLD_MAP_SEA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        EnterArea(
            room_id=R135_SEA_AREA_01_ENTRANCE,
            face_direction=SOUTHWEST,
            x=18,
            y=120,
            z=15,
            run_entrance_event=True,
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceSouth(), ASJumpToHeight(height=0, silent=True)],
        ),
        Return(),
    ]
)
