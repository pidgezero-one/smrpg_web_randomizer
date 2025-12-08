# pylint: disable=C0301

"""E0633_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_EXTERIOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_633_enter_area_4"]),
        Return(),
        EnterArea(
            room_id=R064_MARRYMORE_OUTSIDE,
            face_direction=SOUTHWEST,
            x=18,
            y=64,
            z=6,
            run_entrance_event=True,
            identifier="EVENT_633_enter_area_4"),
        Return(),
    ]
)
