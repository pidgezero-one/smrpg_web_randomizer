# pylint: disable=C0301

"""E3415_TOWER_STACKED_CHESTS_ON_TOP_FLOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_3415_c2"]),
        JmpToEvent(E1936_KEEP_ROTATING_ROOM_CHEST_1),
        JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2, identifier="EVENT_3415_c2"),
    ]
)
