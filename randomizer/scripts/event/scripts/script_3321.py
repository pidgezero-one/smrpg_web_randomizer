# pylint: disable=C0301

"""E3321_VOLCANO_ENTER_1ST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(room_id=R354_VOLCANO_AREA_01, face_direction=SOUTH, x=5, y=87, z=15),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferXYZFSteps(x=0, y=0, z=16, direction=EAST),
                ASJumpToHeight(height=0, silent=True),
            ]),
        Jmp(["EVENT_3323_jmp_if_bit_set_0"]),
    ]
)
