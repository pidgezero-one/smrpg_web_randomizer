# pylint: disable=C0301

"""E1898_ABYSS_BOSS_2_ROOM_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        SetBit(ABYSS_FINAL_ROOM_TRAMPOLINE),
        EnterArea(
            room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
            face_direction=SOUTH,
            x=20,
            y=35,
            z=8,
            run_entrance_event=True),
        Return(),
    ]
)
