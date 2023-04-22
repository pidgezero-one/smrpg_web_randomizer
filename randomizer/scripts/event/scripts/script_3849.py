# pylint: disable=C0301

"""E3849_WORLD_MAP_ROSE_WAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        StopAllBackgroundEvents(),
        Db(bytearray(b"\xfdD")),
        Db(bytearray(b"\xfdE")),
        JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 18, ["EVENT_3849_set_short_7"]),
        SetVarToConst(UNKNOWN_7036, 0),
        EnterArea(
            room_id=R079_ROSE_WAY_MAIN_AREA,
            face_direction=NORTHEAST,
            x=4,
            y=56,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetVarToConst(UNKNOWN_7036, 4493, identifier="EVENT_3849_set_short_7"),
        EnterArea(
            room_id=R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED,
            face_direction=SOUTHWEST,
            x=26,
            y=77,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
