# pylint: disable=C0301

"""E1571_MIDAS_RIVER_BARREL_SECTION_BUSINESS_LOGIC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(UNKNOWN_MIDAS_RIVER_7078_2),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7026, 22),
        SetVarToConst(TEMP_7028, 21),
        RunBackgroundEvent(
            event_id=E1585_MIDAS_RIVER_BARREL_SUBROUTINE, return_on_level_exit=True
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftSouthSteps(4)]),
        FreezeCamera(),
        Db(bytearray(b"\xc7\x95")),
        SetAsyncActionScript(NPC_9, A0170_MIDAS_BARRELS_WATER_SPLASH),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkSouthwestPixels(4),
                ASWalkNortheastSteps(2),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=13, y=16, z=17, direction=EAST),
                ASFaceSouthwest(),
                ASPause(9),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSpriteSequence(
                    index=8, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=0, silent=True),
                ASFloatingOn(),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthwestSteps(2),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(4),
                ASSetWalkingSpeed(FAST),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASJumpToHeight(height=64, silent=True),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPause(20),
                ASResetProperties(),
                ASSetSequenceSpeed(FAST),
                ASSequenceLoopingOn(),
                ASFloatingOn(),
                ASShadowOff(),
            ]),
        SetSyncActionScript(NPC_1, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
        SetSyncActionScript(MARIO, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
        SetSyncActionScript(SCREEN_FOCUS, A0592_MIDAS_BARREL_CAMERA),
        MoveScriptToBackgroundThread2(),
        EnableControlsUntilReturn(
            [A, B], identifier="EVENT_1571_enable_controls_until_return_70"
        ),
        Pause(1, identifier="EVENT_1571_pause_71"),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1571_clear_bit_82"]),
        JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7078_2, ["EVENT_1571_adjust_music_tempo_132"]),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_1571_jmp_if_mario_in_air_77"]
        ),
        Jmp(["EVENT_1571_pause_71"]),
        JmpIfMarioInAir(
            ["EVENT_1571_pause_71"], identifier="EVENT_1571_jmp_if_mario_in_air_77"
        ),
        ClearBit(TEMP_7044_4),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_1571_pause_71"]),
        SetBit(TEMP_7044_4),
        Jmp(["EVENT_1571_pause_71"]),
        ClearBit(TEMP_7044_7, identifier="EVENT_1571_clear_bit_82"),
        PauseActionScript(MARIO),
        PauseActionScript(SCREEN_FOCUS),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfMarioInAir(["EVENT_1571_set_7000_to_7000_short_mem_100"]),
        EnableControlsUntilReturn([]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(4),
                ASSetWalkingSpeed(FAST),
            ]),
        PauseActionScript(MEM_70A9),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
                ASJumpToHeight(height=64, silent=True),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
            ]),
        ResumeActionScript(MARIO),
        StoreSetBits(TEMP_7044_6),
        Pause(19),
        ResumeActionScript(SCREEN_FOCUS),
        Pause(1),
        ActionQueueSync(
            target=MARIO, subscript=[ASSetSequenceSpeed(FAST), ASResetProperties()]
        ),
        AddConstToVar(TEMP_702C, 65526),
        Jmp(["EVENT_1571_enable_controls_until_return_70"]),
        CopyVarToVar(
            from_var=TEMP_7028,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1571_set_7000_to_7000_short_mem_100"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        PauseActionScript(MEM_70A8),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_1571_action_queue_sync_122"]),
        EnableControlsUntilReturn([]),
        PauseActionScript(MEM_70A9),
        Pause(1, identifier="EVENT_1571_pause_106"),
        JmpIfMarioInAir(["EVENT_1571_pause_106"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO043_POP_UP_FROM_WATER, channel=4),
                ASSetSpriteSequence(
                    index=4, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkSouthwestPixels(8),
            ]),
        StoreSetBits(TEMP_7044_6),
        ResumeActionScript(MEM_70A8),
        ResumeActionScript(MARIO),
        Pause(9),
        PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
        Pause(10),
        ResumeActionScript(SCREEN_FOCUS),
        StartLoopNTimes(2),
        PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
        Pause(10),
        EndLoop(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(48),
                ASWalkNortheastPixels(4),
                ASResetProperties(),
            ]),
        Jmp(["EVENT_1571_enable_controls_until_return_70"]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(3)],
            identifier="EVENT_1571_action_queue_sync_122"),
        ResumeActionScript(SCREEN_FOCUS),
        ResetCoords(MARIO),
        ActionQueueAsync(
            target=MARIO, subscript=[ASWalk1StepSouthwest(), ASWalk1StepSouthwest()]
        ),
        SetSyncActionScript(MARIO, A0592_MIDAS_BARREL_CAMERA),
        ActionQueueSync(target=MEM_70A9, subscript=[ASSetAllSpeeds(FAST)]),
        Db(bytearray(b"\xbd\x00\x14")),
        Db(bytearray(b"\xbd\x00\x13")),
        Db(bytearray(b"\xbd\x00\x14")),
        Jmp(["EVENT_1571_pause_71"]),
        SlowDownMusicTempoBy(
            duration=30, change=0, identifier="EVENT_1571_adjust_music_tempo_132"
        ),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        SetSyncActionScript(MEM_70A9, A0592_MIDAS_BARREL_CAMERA),
        SetSyncActionScript(MARIO, A0592_MIDAS_BARREL_CAMERA),
        PauseActionScript(SCREEN_FOCUS),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASWalkSouthwestSteps(14)]),
        FadeOutToBlack(sync=False, duration=32),
        EnterArea(
            room_id=R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA,
            face_direction=SOUTH,
            x=20,
            y=21,
            z=0),
        ClearBit(UNKNOWN_MIDAS_RIVER_7079_1),
        SetBit(TEMP_7043_1),
        JmpToEvent(E3486_MIDAS_RIVER_BASE_AREA_LOADER),
        Return(),
    ]
)
