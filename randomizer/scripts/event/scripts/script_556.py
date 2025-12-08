# pylint: disable=C0301

"""E0556_ROSE_TOWN_LIBERATED_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=1, volume=127),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_556_action_queue_sync_4"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASSetPriority(3)],
            identifier="EVENT_556_action_queue_sync_4"),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_4, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_9, subscript=[ASSetPriority(3)]),
        RememberLastObject(),
        SummonObjectToSpecificLevel(NPC_2, R087_ROSE_TOWN_ITEM_SHOP),
        SummonObjectToSpecificLevel(NPC_3, R087_ROSE_TOWN_ITEM_SHOP),
        SummonObjectToSpecificLevel(NPC_1, R091_ROSE_TOWN_COUPLES_HOUSE),
        RunBackgroundEvent(
            event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND,
            return_on_level_exit=True),
        FadeInFromBlack(sync=False),
        SetBit(TEMP_709F_5),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_556_ret_40"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_556_ret_40"]),
        RunEventAsSubroutine(E3895_ROSE_TOWN_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_556_ret_40"),
    ]
)
