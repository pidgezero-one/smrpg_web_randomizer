# pylint: disable=C0301

"""E3348_KEEP_DOOR_REWARD_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftZUpSteps(2),
                ASPause(8),
                ASShiftZDownSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x0007),
        AddConstToVar(PRIMARY_TEMP_7000, 512),
        Dec(PRIMARY_TEMP_7000),
        SetMem704XAt7000Bit(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_3348_set_13"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 514, ["EVENT_3348_set_15"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 515, ["EVENT_3348_set_17"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 516, ["EVENT_3348_set_19"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 517, ["EVENT_3348_set_21"]),
        JmpToEvent(E1936_KEEP_ROTATING_ROOM_CHEST_1),
        JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2, identifier="EVENT_3348_set_13"),
        JmpToEvent(E1938_KEEP_ROTATING_ROOM_CHEST_3, identifier="EVENT_3348_set_15"),
        JmpToEvent(E1939_KEEP_ROTATING_ROOM_CHEST_4, identifier="EVENT_3348_set_17"),
        JmpToEvent(E1940_KEEP_ROTATING_ROOM_CHEST_5, identifier="EVENT_3348_set_19"),
        JmpToEvent(E1941_KEEP_ROTATING_ROOM_CHEST_6, identifier="EVENT_3348_set_21"),
    ]
)
