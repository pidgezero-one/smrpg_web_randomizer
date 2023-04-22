# pylint: disable=C0301

"""E3612_CHEST_DIFFERENTIATOR_NPC_1_OR_OTHER_CAMERA_B"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3612_chest_2"]),
        JmpToEvent(E3391_VOLCANO_1ST_SAVE_ROOM_LOWER_CHEST),
        JmpToEvent(
            E3392_VOLCANO_1ST_SAVE_ROOM_UPPER_CHEST, identifier="EVENT_3612_chest_2"
        ),
    ]
)
