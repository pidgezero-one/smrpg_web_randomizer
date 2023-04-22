# pylint: disable=C0301

"""E0376_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set0158Bit7Offset(0x0158),
        RunBackgroundEvent(
            event_id=E0392_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_REPEATING_SHYSTERS_POSITION,
            return_on_level_exit=True,
        ),
        JmpIfObjectInSpecificLevel(
            NPC_5,
            R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            ["EVENT_376_jmp_if_object_in_level_6"],
        ),
        PauseActionScript(NPC_9),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASShadowOff(),
                ASTransferToXYZF(x=20, y=118, z=4, direction=EAST),
                ASFaceSouthwest(),
                ASSetSolidityBits(cant_walk_through=True),
            ],
        ),
        SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
        JmpIfObjectInSpecificLevel(
            NPC_6,
            R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            ["EVENT_376_jmp_if_object_in_level_10"],
            identifier="EVENT_376_jmp_if_object_in_level_6",
        ),
        PauseActionScript(NPC_7),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASShadowOff(),
                ASSetSolidityBits(cant_walk_through=True),
                ASSetSolidityBits(bit_4=True),
            ],
        ),
        SetSyncActionScript(NPC_7, A0128_WALK_RANDOM_DIRECTIONS),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            ["EVENT_376_action_queue_sync_12"],
            identifier="EVENT_376_jmp_if_object_in_level_10",
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASShadowOff(),
                ASFaceSouthwest(),
                ASSetSolidityBits(cant_walk_through=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASSetPriority(3)],
            identifier="EVENT_376_action_queue_sync_12",
        ),
        ActionQueueAsync(target=NPC_4, subscript=[ASSetPriority(3)]),
        PlaySound(sound=SO000_SILENCE, channel=4),
        FadeOutMusicToVolume(duration=1, volume=127),
        RunEventAsSubroutine(
            E0762_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_376_ret_4"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_376_ret_4"]),
        RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_376_ret_4"),
    ]
)
