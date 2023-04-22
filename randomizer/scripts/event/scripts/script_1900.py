# pylint: disable=C0301

"""E1900_ABYSS_BIG_CONVEYOR_ROOM_FALL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_1900_pause_0"),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 1792),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1900_pause_0"]),
        Db(bytearray(b"\xfdG")),
        RemoveObjectFromCurrentLevel(MARIO),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        EnterArea(
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            face_direction=SOUTH,
            x=14,
            y=9,
            z=10,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
