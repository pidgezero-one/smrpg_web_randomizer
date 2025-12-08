# pylint: disable=C0301

"""E3860_WORLD_MAP_SHIP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R160_SUNKEN_SHIP_AREA_01,
            face_direction=SOUTH,
            x=4,
            y=18,
            z=8,
            run_entrance_event=True),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceSouth(), ASJumpToHeight(height=0, silent=True)]),
        Return(),
    ]
)
