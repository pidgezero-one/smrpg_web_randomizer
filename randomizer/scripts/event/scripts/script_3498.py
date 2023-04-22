# pylint: disable=C0301

"""E3498_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["EVENT_3498_action_queue_async_5"]),
        SetSyncActionScript(NPC_4, A0045_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_PATH),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetPriority(3),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(NORMAL),
                ASJumpToHeight(128),
                ASWalk1StepSouthwest(),
                ASPause(12),
                ASFloatingOff(),
            ],
            identifier="EVENT_3498_action_queue_async_5",
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASFixedFCoordOn(),
                ASSetAllSpeeds(NORMAL),
                ASJumpToHeight(64),
                ASWalk1StepNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASPlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
                ASSetWalkingSpeed(VERY_FAST),
                ASFixedFCoordOn(),
                ASWalkEastPixels(4),
                ASWalkWestPixels(8),
                ASWalkEastPixels(8),
                ASWalkWestPixels(8),
                ASWalkEastPixels(8),
                ASWalkWestPixels(4),
                ASFaceSoutheast(),
            ],
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 0),
        StartLoopNTimes(7),
        CreatePacketAtObjectCoords(
            packet=P017_SMALL_MINIGAME_COIN,
            target_npc=NPC_1,
            destinations=["EVENT_3498_pause_11"],
        ),
        Pause(1, identifier="EVENT_3498_pause_11"),
        Inc(PRIMARY_TEMP_700C),
        EndLoop(),
        Pause(30),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3498_action_queue_async_18"]),
        SetBit(TEMP_7043_1),
        Jmp(["EVENT_3498_action_queue_async_5"]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
                ASFixedFCoordOff(),
                ASSetAllSpeeds(FAST),
                ASWalkNorthwestSteps(9),
                ASFaceSoutheast(),
            ],
            identifier="EVENT_3498_action_queue_async_18",
        ),
        Pause(180),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASJumpToHeight(0), ASPause(13), ASFloatingOff()],
            identifier="EVENT_3498_action_queue_async_20",
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASBounceToXYWithHeight(x=5, y=90, height=9)]
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 0),
        StartLoopNTimes(7),
        CreatePacketAtObjectCoords(
            packet=P017_SMALL_MINIGAME_COIN,
            target_npc=NPC_3,
            destinations=["EVENT_3498_pause_26"],
        ),
        Pause(1, identifier="EVENT_3498_pause_26"),
        Inc(PRIMARY_TEMP_700C),
        EndLoop(),
        Pause(20),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_3498_ret_41"]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASResetProperties(),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalkWestSteps(2),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=3, y=90, z=8, direction=EAST),
                ASJumpToHeight(0),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASPause(7),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASJumpToHeight(88),
                ASWalkEastSteps(2),
                ASPlaySound(sound=SO065_THWOMP_STOMP, channel=4),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueAsync(target=NPC_2, subscript=[ASShiftZDownPixels(8)]),
        SetBit(TEMP_7043_2),
        Jmp(["EVENT_3498_action_queue_async_20"]),
        Return(identifier="EVENT_3498_ret_41"),
    ]
)
