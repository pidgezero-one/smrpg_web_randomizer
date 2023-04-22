# pylint: disable=C0301

"""E1678_OPEN_LANDS_END_GROTTO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS,
            face_direction=SOUTH,
            x=6,
            y=29,
            z=9,
            run_entrance_event=True,
        ),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Return(),
    ]
)
