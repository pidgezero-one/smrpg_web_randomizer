# pylint: disable=C0301

"""E1427_MUSHROOM_WAY_1_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0202_UNLOCK_FOREST_IF_GATED_BY_MUSHROOM_WAY_CHARACTER),
        ActionQueueAsync(target=NPC_0, subscript=[ASSetPriority(3), ASReturn()]),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_1, ["EVENT_1427_remove_from_current_level_5"]),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_1427_remove_from_current_level_5"]),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_1427_remove_from_current_level_5"]),
        Jmp(["EVENT_1427_jmp_to_event_7"]),
        RemoveObjectFromCurrentLevel(
            NPC_8, identifier="EVENT_1427_remove_from_current_level_5"
        ),
        RemoveObjectFromCurrentLevel(NPC_9),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1427_jmp_to_event_7"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1427_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1427_ret_26"]),
        RunEventAsSubroutine(E3888_MUSHROOM_WAY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1427_ret_26"),
    ]
)
