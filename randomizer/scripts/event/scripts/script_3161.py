# pylint: disable=C0301

"""E3161_MINES_CHECK_IF_SHYGUY_MOVED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseScriptIfMenuOpen(),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM,
            ["EVENT_3161_jmp_4"],
        ),
        EnterArea(
            room_id=R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM,
            face_direction=NORTHEAST,
            x=23,
            y=72,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        Jmp(["EVENT_3198_pause_script_if_menu_open_0"], identifier="EVENT_3161_jmp_4"),
        Return(),
    ]
)
