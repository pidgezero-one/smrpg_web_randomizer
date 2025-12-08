# pylint: disable=C0301

"""E2343_TOWER_SEESAW_ROOM_SET_ORIGIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Z,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2343_set_7000_to_object_coord_0"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2343_clear_bit_4"]),
        Pause(1),
        Jmp(["EVENT_2343_set_7000_to_object_coord_0"]),
        ClearBit(TEMP_7043_1, identifier="EVENT_2343_clear_bit_4"),
        Return(),
    ]
)
