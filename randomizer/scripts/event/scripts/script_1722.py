# pylint: disable=C0301

"""E1722_SKY_BRIDGE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(FLOWER_TOWER_ASCENDED, ["EVENT_1722_action_queue_sync_2"]),
        RemoveObjectFromCurrentLevel(NPC_18),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASShiftZUpPixels(1)],
            identifier="EVENT_1722_action_queue_sync_2"),
        ActionQueueSync(target=NPC_3, subscript=[ASShiftZUpPixels(1)]),
        FadeInFromBlack(sync=True),
        JmpIfBitClear(TEMP_7044_0, ["EVENT_1722_jmp_if_bit_clear_8"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(height=128, silent=True),
                ASWalk1StepSouth(),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(
                    1, identifier="EVENT_1722_action_queue_async_6_SUBSCRIPT_pause_9"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1722_action_queue_async_6_SUBSCRIPT_pause_9"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ]),
        Jmp(["EVENT_1722_set_action_script_sync_10"]),
        JmpIfBitClear(
            TEMP_7043_7,
            ["EVENT_1722_set_action_script_sync_10"],
            identifier="EVENT_1722_jmp_if_bit_clear_8"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(height=108, silent=True),
                ASWalk1StepSouth(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_1722_action_queue_async_9_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1722_action_queue_async_9_SUBSCRIPT_pause_6"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ]),
        SetSyncActionScript(
            MARIO,
            A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM,
            identifier="EVENT_1722_set_action_script_sync_10"),
        SetBit(SKY_BRIDGE_COURSE_CHOICE),
        SetBit(SKY_BRIDGE_COURSE_1_CHOSEN),
        SetVarToConst(TEMP_702E, 48),
        SetVarToConst(TEMP_702C, 70),
        ActionQueueSync(
            target=NPC_16,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthPixels(16),
                ASPause(
                    300, identifier="EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_2"
                ),
                ASShiftZDownPixels(16),
                ASPause(
                    1, identifier="EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_4"
                ),
                ASSetVarToConst(TEMP_7034, 32774),
                ASCreatePacketAtObjectCoords(
                    packet=P032_BLUE_CLOUD,
                    target_npc=DUMMY_0X07,
                    destinations=["EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_4"]),
                ASPause(120),
                ASShiftZUpPixels(16),
                ASJmp(["EVENT_1722_action_queue_sync_15_SUBSCRIPT_pause_2"]),
            ]),
        Return(),
    ]
)
