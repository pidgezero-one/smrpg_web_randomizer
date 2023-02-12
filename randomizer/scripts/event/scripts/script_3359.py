# E3359_KEEP_INITIATE_COIN_GAME

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetPriority(3),
                ASWalkToXYCoords(x=23, y=81),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetPriority(3),
                ASShiftZUpSteps(4),
                ASWalkToXYCoords(x=24, y=79),
            ],
        ),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftNortheastSteps(4)]),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        SetBit(TEMP_7044_7),
        SetVarToConst(ROSE_WAY_703C, 21),
        PlayMusicAtDefaultVolume(M36_EXPLANATION),
        FreezeCamera(),
        MoveScriptToBackgroundThread2(),
        SetVarToConst(ROSE_WAY_703A, 4, identifier="EVENT_3359_set_short_13"),
        ActionQueueAsync(target=NPC_1, subscript=[ASShiftNortheastSteps(3)]),
        Pause(1, identifier="EVENT_3359_pause_15"),
        Set7000ToTappedButton(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3359_dec_short_21"]),
        JmpIfVarEqualsConst(ROSE_WAY_703A, 4, ["EVENT_3359_pause_15"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 32, ["EVENT_3359_action_queue_async_26"]
        ),
        Jmp(["EVENT_3359_pause_15"]),
        Dec(ROSE_WAY_703A, identifier="EVENT_3359_dec_short_21"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(108),
                ASPause(
                    1, identifier="EVENT_3359_action_queue_async_22_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3359_action_queue_async_22_SUBSCRIPT_pause_1"]
                ),
                ASPause(8),
            ],
        ),
        JmpIfVarEqualsConst(ROSE_WAY_703C, 0, ["EVENT_3359_resume_action_script_61"]),
        JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["EVENT_3359_action_queue_async_26"]),
        Jmp(["EVENT_3359_pause_15"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASShiftSouthwestSteps(3)],
            identifier="EVENT_3359_action_queue_async_26",
        ),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASFixedFCoordOn(),
                ASStartLoopNTimes(1),
                ASJumpToHeight(48),
                ASWalk1StepSouthwest(),
                ASEndLoop(),
            ],
        ),
        SetBit(TEMP_7044_7),
        SetVarToRandom(ROSE_WAY_703A, 4),
        Inc(ROSE_WAY_703A),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPlaySound(sound=SO004_JUMP, channel=4),
                ASJumpToHeight(80),
                ASPause(3),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASPause(10),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            ],
            identifier="EVENT_3359_action_queue_sync_33",
        ),
        Pause(8),
        RunBackgroundEvent(
            event_id=E3360_KEEP_COIN_GAME_CHEST, return_on_level_exit=True
        ),
        Pause(32),
        JmpIfVarEqualsConst(ROSE_WAY_703C, 0, ["EVENT_3359_resume_action_script_42"]),
        Dec(ROSE_WAY_703A),
        JmpIfVarNotEqualsConst(ROSE_WAY_703A, 0, ["EVENT_3359_action_queue_sync_33"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASStartLoopNTimes(1),
                ASJumpToHeight(48),
                ASWalk1StepNortheast(),
                ASEndLoop(),
            ],
        ),
        Jmp(["EVENT_3359_set_short_13"]),
        ResumeActionScript(NPC_2, identifier="EVENT_3359_resume_action_script_42"),
        Pause(16),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
        Pause(16),
        PlayMusicAtDefaultVolume(M09_VICTORY),
        SetBit(TEMP_7044_7),
        Pause(32),
        UnfreezeCamera(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShiftZUpSteps(5),
                ASWalkToXYCoords(x=29, y=70),
                ASShiftZDownSteps(2),
                ASShiftZDownPixels(8),
            ],
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING,
            mod_id=0,
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(32), ASWalk1StepNortheast()]
        ),
        SetVarToConst(ROSE_WAY_703E, 0),
        JmpToEvent(E1955_KEEP_COIN_GAME_ROOM_EXIT_CONTAINER),
        Return(),
        ResumeActionScript(NPC_2, identifier="EVENT_3359_resume_action_script_61"),
        Pause(8),
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
        Pause(8),
        PlayMusicAtDefaultVolume(M66_BOWSERS_CASTLE_2ND_TIME),
        SlowDownMusic(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(2),
            ],
        ),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        RunDialog(
            dialog_id=DI1907_DUPLICATE,
            above_object=NPC_14,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        SetBit(TEMP_7044_7),
        Pause(240),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
    ]
)
