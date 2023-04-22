# pylint: disable=C0301

"""E1712_BANDITS_WAY_2_DOG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        SetVarToConst(BATTLE_PACK_ID, 9),
        StartBattleWithPackAt700E(),
        ClearBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        ActionQueueSync(
            target=MARIO, subscript=[ASPause(3), ASJumpToHeight(height=0, silent=True)]
        ),
        SetVarToConst(TEMP_70AB, 20),
        StartLoopNTimes(1),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1712_inc_16"]),
        JmpIfObjectNotInSpecificLevel(
            MEM_70AB, R207_BANDITS_WAY_AREA_02, ["EVENT_1712_action_queue_async_13"]
        ),
        Jmp(["EVENT_1712_inc_16"]),
        ActionQueueAsync(
            target=MEM_70AB,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASDb(bytearray(b"\xfd\x12")),
                ASSet700CToObjectCoord(
                    target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True
                ),
                ASCompareVarToConst(PRIMARY_TEMP_700C, 14),
                ASJmpIfComparisonResultIsLesser(
                    ["EVENT_1712_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_9"]
                ),
                ASTransferToXYZF(x=8, y=74, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceNortheast(),
                ASJmp(
                    ["EVENT_1712_action_queue_async_13_SUBSCRIPT_set_solidity_bits_12"]
                ),
                ASTransferToXYZF(
                    x=18,
                    y=73,
                    z=0,
                    direction=EAST,
                    identifier="EVENT_1712_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_9",
                ),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASSetSolidityBits(
                    bit_4=True,
                    cant_walk_through=True,
                    identifier="EVENT_1712_action_queue_async_13_SUBSCRIPT_set_solidity_bits_12",
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
            identifier="EVENT_1712_action_queue_async_13",
        ),
        SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
        SummonObjectToSpecificLevel(MEM_70AB, R207_BANDITS_WAY_AREA_02),
        Inc(TEMP_70AB, identifier="EVENT_1712_inc_16"),
        EndLoop(),
        RunBackgroundEvent(
            event_id=E1705_BANDITS_WAY_2_DOGS_BACKGROUND, return_on_level_exit=True
        ),
        Return(),
    ]
)
