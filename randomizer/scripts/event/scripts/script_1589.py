# pylint: disable=C0301

"""E1589_LANDS_END_GROTTO_TRAMPOLINE_TO_SURFACE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R142_LANDS_END_AREA_05_SKY_BRIDGE,
            face_direction=SOUTH,
            x=10,
            y=80,
            z=3,
        ),
        SetBit(TEMP_7044_0),
        JmpToEvent(E1722_SKY_BRIDGE_ROOM_LOADER),
    ]
)
