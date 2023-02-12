# E0372_MUSHROOM_KINGDOM_BOSS_FIGHT_CUTSCENE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNUSED_7082_4, ["EVENT_256_ret_0"]),
        SetBit(UNUSED_7082_4),
        SetBit(TEMP_7043_5),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_372_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(["EVENT_372_action_queue_async_3_SUBSCRIPT_pause_0"]),
                ASFloatingOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASBounceToXYWithHeight(x=15, y=31, height=4),
                ASFaceNortheast(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
            ],
        ),
        RememberLastObject(),
        Pause(60),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_8, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        ActionQueueSync(target=MARIO, subscript=[ASPause(30), ASFaceNorthwest()]),
        RememberLastObject(),
        SetBit(TEMP_7043_5),
        Pause(30),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_9, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        ActionQueueSync(target=MARIO, subscript=[ASPause(30), ASFaceSoutheast()]),
        RememberLastObject(),
        SetBit(TEMP_7043_5),
        Pause(30),
        ClearBit(TEMP_7043_5),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(bit_4=True),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x07p\xff")),
                ASShiftSoutheastPixels(15),
                ASSetWalkingSpeed(FAST),
                ASShiftSoutheastPixels(10),
                ASBPL262728(),
                ASFixedFCoordOn(),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=6),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=80, silent=True),
                ASFloatingOn(),
                ASWalk1StepNorthwest(),
                ASShiftNorthwestPixels(9),
                ASPause(
                    1, identifier="EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_17"
                ),
                ASJmpIfObjectInAir(
                    NPC_8, ["EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_17"]
                ),
                ASJumpToHeight(height=64, silent=True),
                ASWalk1StepNorthwest(),
                ASPause(
                    1, identifier="EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_21"
                ),
                ASJmpIfObjectInAir(
                    NPC_8, ["EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_21"]
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASClearSolidityBits(bit_4=True),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x07p\xff")),
                ASShiftNorthwestPixels(15),
                ASSetWalkingSpeed(FAST),
                ASShiftNorthwestPixels(10),
                ASBPL262728(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=80, silent=True),
                ASFloatingOn(),
                ASWalk1StepSoutheast(),
                ASShiftSoutheastPixels(9),
                ASPause(
                    1, identifier="EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_15"
                ),
                ASJmpIfObjectInAir(
                    NPC_9, ["EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_15"]
                ),
                ASJumpToHeight(height=64, silent=True),
                ASWalk1StepSoutheast(),
                ASPause(
                    1, identifier="EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_19"
                ),
                ASJmpIfObjectInAir(
                    NPC_9, ["EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_19"]
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(10),
                ASFaceNortheast(),
                ASSetSpriteSequence(
                    index=16,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(30),
                ASResetProperties(),
            ],
        ),
        RememberLastObject(),
        ActionQueueSync(target=NPC_4, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_5, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_6, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_7, subscript=[ASFaceSouthwest()]),
        RememberLastObject(),
        Pause(60),
        SetSyncActionScript(NPC_4, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_5, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_8, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_9, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_6, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_7, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        Pause(60),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepNortheast()]),
        Jmp(["EVENT_373_action_queue_sync_6"]),
    ]
)
