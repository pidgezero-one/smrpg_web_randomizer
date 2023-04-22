# pylint: disable=C0301

"""E0371_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set0158Bit7Offset(0x015C),
        Set0158Bit7Offset(0x015E),
        RunBackgroundEvent(
            event_id=E0377_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_REPEATING_SHYSTERS_POSITION,
            return_on_level_exit=True,
            bit_6=True,
        ),
        RunEventAsSubroutine(
            E0765_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
