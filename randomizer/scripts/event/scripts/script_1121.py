# pylint: disable=C0301

"""E1121_SEASIDE_OCCUPIED_INN_1F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0807_SEASIDE_OCCUPIED_INN_1F_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1121_run_event_as_subroutine_3"]),
        FadeInFromBlack(sync=False),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_1121_run_event_as_subroutine_3"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1121_ret_4"]),
        RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1121_ret_4"),
    ]
)
