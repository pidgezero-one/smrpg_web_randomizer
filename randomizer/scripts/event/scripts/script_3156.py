# pylint: disable=C0301

"""E3156_MINECART_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunBackgroundEvent(
            event_id=E3157_MINECART_ROOM_LOADER_BACKGROUND, return_on_level_exit=True
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
