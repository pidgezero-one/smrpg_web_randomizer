# pylint: disable=C0301

"""E1071_BEGIN_MELODY_BAY_TADPOLES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(NORMAL),
                ASWalkToXYCoords(x=7, y=48),
                ASWalkNortheastPixels(3),
                ASWalkNorthwestPixels(2),
                ASFaceNortheast(),
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetPriority(3),
                ASSetVRAMPriority(PRIORITY_3),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASBounceToXYWithHeight(x=4, y=32, height=0),
            ]),
        FreezeCamera(),
        JmpIfBitClear(TEMP_7044_2, ["EVENT_1071_set_short_33"]),
        JmpIfBitSet(TOADOFSKY_REMOVED, ["EVENT_1071_jmp_if_bit_clear_9"]),
        JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1071_jmp_if_bit_clear_9"]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASShiftToXYCoords(x=14, y=25),
                ASSetSequenceSpeed(VERY_SLOW),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkSouthwestPixels(6),
                ASSequenceLoopingOn(),
            ]),
        JmpIfBitClear(
            TEMP_7043_0,
            ["EVENT_1071_jmp_if_bit_clear_12"],
            identifier="EVENT_1071_jmp_if_bit_clear_9"),
        SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_1,
            ["EVENT_1071_jmp_if_bit_clear_15"],
            identifier="EVENT_1071_jmp_if_bit_clear_12"),
        SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_2,
            ["EVENT_1071_jmp_if_bit_clear_18"],
            identifier="EVENT_1071_jmp_if_bit_clear_15"),
        SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_3,
            ["EVENT_1071_jmp_if_bit_clear_21"],
            identifier="EVENT_1071_jmp_if_bit_clear_18"),
        SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_4,
            ["EVENT_1071_jmp_if_bit_clear_24"],
            identifier="EVENT_1071_jmp_if_bit_clear_21"),
        SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_5,
            ["EVENT_1071_jmp_if_bit_clear_27"],
            identifier="EVENT_1071_jmp_if_bit_clear_24"),
        SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_6,
            ["EVENT_1071_jmp_if_bit_clear_30"],
            identifier="EVENT_1071_jmp_if_bit_clear_27"),
        SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        JmpIfBitClear(
            TEMP_7043_7,
            ["EVENT_1071_set_short_33"],
            identifier="EVENT_1071_jmp_if_bit_clear_30"),
        SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
        Pause(10),
        SetVarToConst(X_COORD_1, 3, identifier="EVENT_1071_set_short_33"),
        SetVarToConst(TEMP_70A9, 20),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=6, y=43, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_0, A0570_MELODY_BAY_TADPOLE_SWIMS),
        JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1071_jmp_38"]),
        JmpIfBitSet(
            MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1071_third_song_not_unlocked_yet"]
        ),
        JmpIfBitSet(
            MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1071_second_song_not_unlocked_yet"]
        ),
        JmpToEvent(E1082_MELODY_BAY_SONG_1_INPUT),
        JmpIfBitClear(
            MINECART_CLEARED,
            ["EVENT_1071_jmp_38"],
            identifier="EVENT_1071_second_song_not_unlocked_yet"),
        JmpToEvent(E1083_MELODY_BAY_SONG_2_INPUT),
        JmpIfBitClear(
            MINECART_CLEARED,
            ["EVENT_1071_jmp_38"],
            identifier="EVENT_1071_third_song_not_unlocked_yet"),
        JmpToEvent(E1084_MELODY_BAY_SONG_3_INPUT),
        JmpToEvent(E1073_MELODY_BAY_JUMP_ON_TADPOLES, identifier="EVENT_1071_jmp_38"),
        Return(),
    ]
)
