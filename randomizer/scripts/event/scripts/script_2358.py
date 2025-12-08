# pylint: disable=C0301

"""E2358_TOWER_THWOMP_SEESAW_ROOM_LOADER_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2358_pause_0"),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2358_clear_bit_11"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_2358_set_7000_to_object_coord_5"]
        ),
        Jmp(["EVENT_2358_pause_0"]),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_X,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2358_set_7000_to_object_coord_5"),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 18, ["EVENT_2358_set_7000_to_object_coord_9"]
        ),
        ClearBit(TEMP_7043_1),
        Return(),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2358_set_7000_to_object_coord_9"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_2358_pause_0"]),
        ClearBit(TEMP_7043_1, identifier="EVENT_2358_clear_bit_11"),
        Return(),
    ]
)
