# pylint: disable=C0301

"""E3227_SHIP_CLONE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
            ["EVENT_3227_run_event_as_subroutine_32"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 16, ["EVENT_3227_run_background_event_4"]
        ),
        ActionQueueAsync(target=NPC_0, subscript=[ASShiftToXYCoords(x=19, y=117)]),
        RunBackgroundEvent(
            event_id=E3228_SHIP_CLONE_CONTROL,
            return_on_level_exit=True,
            identifier="EVENT_3227_run_background_event_4"),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER,
            identifier="EVENT_3227_run_event_as_subroutine_32"),
        Return(),
    ]
)
