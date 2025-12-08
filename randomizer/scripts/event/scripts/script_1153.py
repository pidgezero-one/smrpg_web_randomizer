# pylint: disable=C0301

"""E1153_SEASIDE_LIBERATED_INN_1F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(SEASIDE_SHED_EMPTIED, ["EVENT_1153_remove_from_current_level_2"]),
        Jmp(["EVENT_1153_jmp_if_bit_set_4"]),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_1153_remove_from_current_level_2"
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_1153_run_event_as_subroutine_7"],
            identifier="EVENT_1153_jmp_if_bit_set_4"),
        FadeInFromBlack(sync=False),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_1153_run_event_as_subroutine_7"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1153_ret_8"]),
        RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1153_ret_8"),
    ]
)
