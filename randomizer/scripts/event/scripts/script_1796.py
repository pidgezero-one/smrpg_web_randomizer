# pylint: disable=C0301

"""E1796_LANDS_END_DESERT_1_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R142_LANDS_END_AREA_05_SKY_BRIDGE,
            face_direction=SOUTH,
            x=10,
            y=74,
            z=9,
        ),
        SetBit(TEMP_7043_7),
        JmpToEvent(E1722_SKY_BRIDGE_ROOM_LOADER),
    ]
)
