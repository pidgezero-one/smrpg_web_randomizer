# pylint: disable=C0301

"""E3522_CHEST_DIFFERENTIATOR_NPC_9_OR_OTHER_CAMERA_A"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_3522_chest_2"]),
        JmpToEvent(E1936_KEEP_ROTATING_ROOM_CHEST_1),
        JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2, identifier="EVENT_3522_chest_2"),
    ]
)
