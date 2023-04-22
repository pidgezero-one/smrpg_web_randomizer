# pylint: disable=C0301

"""E0561_PLACE_LINK_IN_ROSE_TOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7042_0, ["EVENT_561_action_queue_async_2"]),
        JmpToSubroutine(["EVENT_273_set_bit_92"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetPriority(2)],
            identifier="EVENT_561_action_queue_async_2",
        ),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_561_jmp_to_event_3"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0265_OCCUPIED_MK_INN_LOADER, identifier="EVENT_561_jmp_to_event_3"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_561_ret_7"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_561_ret_7"]),
        RunEventAsSubroutine(E3895_ROSE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_561_ret_7"),
    ]
)
