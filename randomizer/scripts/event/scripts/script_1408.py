# pylint: disable=C0301

"""E1408_MARIOS_PAD_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(4),
        JmpIfBitClear(TEMP_7042_0, ["EVENT_1408_action_queue_sync_3"]),
        ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=33),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASSetPriority(3), ASReturn()],
            identifier="EVENT_1408_action_queue_sync_3"),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1408_run_event_as_subroutine_25"]),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_1408_jmp_if_bit_clear_7"]),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_1408_run_event_as_subroutine_25"),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT,
            ["EVENT_1408_ret_26"],
            identifier="EVENT_1408_jmp_if_bit_clear_7"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1408_ret_26"]),
        RunEventAsSubroutine(E3887_MARIOS_PAD_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1408_ret_26"),
    ]
)
