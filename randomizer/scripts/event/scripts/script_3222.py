# pylint: disable=C0301

"""E3222_SHIP_TROOPA_PUZZLE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        RunBackgroundEvent(
            event_id=E3223_SHIP_TROOPA_PUZZLE, return_on_level_exit=True
        ),
        Return(),
    ]
)
