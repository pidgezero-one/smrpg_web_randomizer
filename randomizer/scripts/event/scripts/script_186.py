# pylint: disable=C0301

"""E0186_PARTY_JOIN_LOGIC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_186_room_154_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 205, ["EVENT_186_room_205_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_186_room_232_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 284, ["EVENT_186_room_284_logic"]),
        Return(),
        JmpToEvent(
            E0197_TOADSTOOL_JOINS_CONTAINER, identifier="EVENT_186_room_154_logic"
        ),
        JmpToEvent(E0194_MALLOW_JOINS_CONTAINER, identifier="EVENT_186_room_205_logic"),
        JmpToEvent(E0195_GENO_JOINS_CONTAINER, identifier="EVENT_186_room_232_logic"),
        JmpToEvent(E0196_BOWSER_JOINS_CONTAINER, identifier="EVENT_186_room_284_logic"),
    ]
)
