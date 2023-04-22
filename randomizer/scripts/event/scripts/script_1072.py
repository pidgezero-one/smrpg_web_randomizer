# pylint: disable=C0301

"""E1072_MELODY_BAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlayMusicAtDefaultVolume(M17_TADPOLE_POND),
        DeactivateSoundChannels([0, 1, 2, 3]),
        JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1072_action_queue_async_18"]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(VERY_SLOW),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSequenceLoopingOn(),
                ASWalkSouthwestPixels(6),
            ],
        ),
        JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1072_clear_bit_14"]),
        JmpIfBitClear(MINECART_CLEARED, ["EVENT_1072_set_bit_9"]),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1072_clear_bit_14"]),
        JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_1072_set_bit_9"]),
        Jmp(["EVENT_1072_clear_bit_14"]),
        SetBit(TOADOFSKY_REMOVED, identifier="EVENT_1072_set_bit_9"),
        RemoveObjectFromCurrentLevel(NPC_8),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
        FadeInFromBlack(sync=False),
        Return(),
        ClearBit(TOADOFSKY_REMOVED, identifier="EVENT_1072_clear_bit_14"),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASShiftToXYCoords(x=15, y=27),
                ASWalkSoutheastPixels(6),
                ASWalkSouthwestPixels(6),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(SLOW),
                ASFaceSouthwest(),
            ],
            identifier="EVENT_1072_action_queue_async_18",
        ),
        ClearBit(TOADOFSKY_REMOVED),
        DeactivateSoundChannels([0, 1, 2, 3]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1072_clear_bit_24"]),
        FadeInFromBlack(sync=False),
        Return(),
        ClearBit(TEMP_7043_0, identifier="EVENT_1072_clear_bit_24"),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7043_5),
        ClearBit(TEMP_7043_6),
        ClearBit(TEMP_7043_7),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1072_ret_26"]),
        RunEventAsSubroutine(E3893_TADPOLE_POND_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1072_ret_26"),
    ]
)
