# pylint: disable=C0301

"""E0531_ROSE_TOWN_OCCUPIED_INN_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CloseDialog(),
        Db(bytearray(b"\xfdG")),
        ActionQueueAsync(target=NPC_1, subscript=[ASSetPriority(2)]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_531_clear_bit_0"]),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_531_run_event_as_subroutine_6"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT, identifier="EVENT_531_clear_bit_0"),
        RunEventAsSubroutine(
            E0265_OCCUPIED_MK_INN_LOADER,
            identifier="EVENT_531_run_event_as_subroutine_6",
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_531_ret_7"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_531_ret_7"]),
        RunEventAsSubroutine(E3895_ROSE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_531_ret_7"),
    ]
)
