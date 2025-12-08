# pylint: disable=C0301

"""E3373_KEEP_THWOMP_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM,
            mod_id=32),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        RunBackgroundEvent(
            event_id=E3374_KEEP_THWOMP_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        Return(),
    ]
)
