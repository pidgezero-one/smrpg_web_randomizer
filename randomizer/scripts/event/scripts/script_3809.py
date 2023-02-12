# E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            mod_id=0,
        ),
        SetBit(TEMP_704C_0),
        EnterArea(
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            face_direction=NORTHEAST,
            x=9,
            y=100,
            z=0,
            run_entrance_event=True,
        ),
        SetBit(CHAPEL_ITEM_RETRIEVAL_STARTED),
        FreezeCamera(),
        RunEventAsSubroutine(
            E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASVisibilityOn(),
                ASTransferXYZFPixels(x=252, y=248, z=0, direction=EAST),
                ASPause(12),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASShiftNortheastPixels(8),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNortheastSteps(13),
                ASShiftNortheastPixels(8),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASShiftNortheastSteps(3),
                ASSetSpriteSequence(
                    index=12,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASSetWalkingSpeed(FASTEST),
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
                ASShiftNortheastPixels(2),
                ASShiftSouthwestPixels(4),
                ASShiftNortheastPixels(4),
                ASShiftSouthwestPixels(4),
                ASShiftNortheastPixels(3),
                ASShiftSouthwestPixels(2),
                ASShiftNortheastPixels(2),
                ASShiftSouthwestPixels(1),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASVisibilityOn(),
                ASTransferXYZFPixels(x=8, y=4, z=6, direction=EAST),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
                ASPause(96),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASJumpToHeight(height=112, silent=True),
                ASSetWalkingSpeed(FAST),
                ASShiftSouthwestSteps(2),
                ASFloatingOn(),
                ASShiftSouthwestSteps(2),
                ASShiftSouthwestPixels(12),
                ASSetSpriteSequence(
                    index=1,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASTransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASShiftNortheastSteps(8),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[1]),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASShiftNortheastSteps(8),
                ASShiftNortheastPixels(2),
                ASShiftSouthwestPixels(4),
                ASShiftNortheastPixels(4),
                ASShiftSouthwestPixels(4),
                ASShiftNortheastPixels(3),
                ASShiftSouthwestPixels(2),
                ASShiftNortheastPixels(2),
                ASShiftSouthwestPixels(1),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(VERY_FAST),
                ASShiftNortheastSteps(8),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASShiftNortheastSteps(8),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=6),
                ASJumpToHeight(height=128, silent=True),
                ASSetWalkingSpeed(FAST),
                ASShiftSouthwestSteps(5),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNortheastSteps(24),
                ASSetWalkingSpeed(FASTEST),
                ASShiftNortheastPixels(8),
                ASShiftSouthwestPixels(16),
                ASShiftNortheastPixels(16),
                ASShiftSouthwestPixels(16),
                ASShiftNortheastPixels(12),
                ASShiftSouthwestPixels(8),
                ASShiftNortheastPixels(8),
                ASShiftSouthwestPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPause(30),
                ASTransferToObjectXY(NPC_8),
                ASTransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
                ASSetPriority(3),
                ASJumpToHeight(height=144, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\xf6\x80\xfd")),
                ASPause(60),
                ASBPL262728(),
                ASTransferToXYZF(x=11, y=86, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(34),
                ASTransferToObjectXY(NPC_8),
                ASTransferXYZFPixels(x=0, y=8, z=12, direction=EAST),
                ASSetPriority(3),
                ASJumpToHeight(height=136, silent=True),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftEastSteps(4),
            ],
        ),
        FadeInFromBlack(sync=True),
        Pause(28),
        ReturnFD(),
        Pause(20),
        ReturnFD(),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASPause(48),
                ASTransferToObjectXY(NPC_8),
                ASTransferXYZFPixels(x=0, y=12, z=14, direction=EAST),
                ASSetPriority(3),
                ASJumpToHeight(height=152, silent=True),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftWestSteps(5),
                ASVisibilityOn(),
            ],
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASPause(60),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=5,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        Pause(10),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASPause(40),
                ASResetProperties(),
                ASPause(8),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=13, is_sequence=True, looping=True),
            ],
        ),
        Pause(30),
        UnfreezeCamera(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOff(),
                ASFaceNortheast(),
                ASShiftNortheastSteps(13),
                ASPause(20),
                ASShiftNortheastSteps(1),
            ],
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPause(44),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(FAST),
                ASShadowOff(),
                ASAddZCoord1Step(),
                ASPause(20),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNortheastSteps(1),
            ],
        ),
        RememberLastObject(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASPause(30),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepNorth(),
                ASFaceNortheast(),
                ASSetSequenceSpeed(SLOW),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepEast(),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPause(10),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x04\x00\xff")),
                ASJumpToHeight(height=104, silent=True),
                ASPause(10),
                ASFloatingOn(),
                ASPause(14),
                ASBPL262728(),
                ASPause(30),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=13, is_sequence=True, looping=True),
            ],
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASSetWalkingSpeed(NORMAL), ASWalk1StepNortheast()]
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASResetProperties(),
                ASFaceSoutheast(),
                ASPause(2),
                ASFaceSouthwest(),
                ASPause(10),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(8),
                ASResetProperties(),
            ],
        ),
        RememberLastObject(),
        ActionQueueAsync(target=NPC_7, subscript=[ASFaceSoutheast()]),
        Pause(10),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASShiftSoutheastPixels(10),
            ],
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(120),
                ASResetProperties(),
                ASFixedFCoordOn(),
                ASShiftNorthwestPixels(10),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
            ],
        ),
        Pause(40),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASSetWalkingSpeed(NORMAL), ASWalk1StepNortheast()]
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASSetWalkingSpeed(NORMAL), ASWalk1StepNortheast()]
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(10),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(8),
                ASResetProperties(),
            ],
        ),
        Pause(60),
        ActionQueueSync(target=NPC_0, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_1, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_2, subscript=[ASFaceSouthwest()]),
        Pause(60),
        ActionQueueSync(
            target=NPC_0, subscript=[ASFaceNortheast(), ASSetSequenceSpeed(FAST)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASFaceNortheast(), ASSetSequenceSpeed(FAST)]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASFaceNortheast(), ASSetSequenceSpeed(FAST)]
        ),
        RememberLastObject(),
        Pause(10),
        ActionQueueSync(target=NPC_0, subscript=[ASSetSequenceSpeed(SLOW)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetSequenceSpeed(SLOW)]),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASWalk1StepNortheast(), ASSetSequenceSpeed(FAST)]
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASShiftSoutheastPixels(10),
                ASPause(30),
                ASShiftNorthwestPixels(14),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPause(50),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASSetWalkingSpeed(SLOW),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalk1StepNorthwest(),
                ASFaceNortheast(),
                ASSetSpriteSequence(
                    index=14, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        RememberLastObject(),
        Pause(30),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASSetWalkingSpeed(NORMAL), ASWalk1StepNortheast()]
        ),
        Pause(20),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(30),
        ActionQueueAsync(target=NPC_7, subscript=[ASFaceSouthwest()]),
        Pause(10),
        ActionQueueSync(target=NPC_0, subscript=[ASPause(30), ASFaceSouthwest()]),
        ActionQueueSync(
            target=NPC_2, subscript=[ASPause(30), ASFaceSouthwest(), ASFixedFCoordOn()]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASPause(30), ASFaceSouthwest(), ASFixedFCoordOff()]
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASPause(140),
                ASVisibilityOff(),
                ASPlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASWalk1StepSoutheast(),
                ASSetSequenceSpeed(NORMAL),
                ASFaceSouthwest(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASWalk1StepNorthwest(),
                ASShiftNorthwestPixels(2),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkToXYCoords(x=20, y=75),
                ASFixedFCoordOff(),
                ASShiftSouthwestSteps(15),
                ASShiftNorthwestSteps(3),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(10),
                ASWalkToXYCoords(x=20, y=75),
                ASFixedFCoordOff(),
                ASShiftSouthwestSteps(9),
                ASShiftNorthwestSteps(4),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(16),
                ASWalkToXYCoords(x=20, y=75),
                ASShiftSouthwestSteps(3),
                ASShiftNorthwestSteps(3),
                ASSetSequenceSpeed(SLOW),
                ASPause(60),
                ASSetBit(TEMP_7043_0),
                ASPause(30),
                ASClearBit(TEMP_7043_0),
                ASSetSequenceSpeed(FAST),
                ASShiftSoutheastSteps(3),
                ASSetSequenceSpeed(SLOW),
                ASFaceNortheast(),
            ],
        ),
        Pause(50),
        SetSyncActionScript(SCREEN_FOCUS, A0214_SANCTUARY_CAMERA),
        Pause(60),
        StopAllBackgroundEvents(),
        ActionQueueSync(target=MARIO, subscript=[ASFaceNortheast()]),
        Pause(10),
        Pause(1, identifier="EVENT_3809_await_camera__"),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_await_camera__"]),
        SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASShiftSoutheastSteps(8),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        Pause(10),
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RemoveObjectFromCurrentLevel(NPC_4),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(30),
                ASSetSequenceSpeed(FAST),
                ASShiftNorthwestSteps(4),
                ASSetSequenceSpeed(SLOW),
                ASFaceNortheast(),
            ],
        ),
        Pause(20),
        Pause(1, identifier="EVENT_3809_await_camera_"),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_await_camera_"]),
        SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
        Pause(10),
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RemoveObjectFromCurrentLevel(NPC_3),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASPause(60),
                ASSetSequenceSpeed(FAST),
                ASShiftSoutheastSteps(3),
                ASSetSequenceSpeed(SLOW),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToObjectXYZ(NPC_7),
                ASShiftZUpSteps(2),
                ASSetSolidityBits(
                    cant_jump_through=True, bit_4=True, cant_walk_through=True
                ),
            ],
        ),
        Pause(30),
        SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
        SetBit(TEMP_7049_2),
        Pause(1, identifier="EVENT_3809_await_camera"),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3809_await_camera"]),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        RememberLastObject(),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNortheast()],
        ),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_0),
        SetSyncActionScript(
            NPC_1,
            A0373_SANCTUARY_HENCHMAN,
            identifier="EVENT_3809_set_action_script_sync_384",
        ),
        SetSyncActionScript(NPC_0, A0372_SANCTUARY_HENCHMAN),
        SetSyncActionScript(NPC_2, A0374_SANCTUARY_HENCHMAN),
        SpeedUpMusicTempoBy(duration=0, change=12),
        SetVarToConst(TEMP_70AE, 8),
        SetVarToConst(TEMP_70AF, 0),
        SetVarToConst(FACTORY_FALL_1, 0),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        ClearBit(SANCTUARY_LOCKED),
        SetVarToConst(TIMER_701C, 300),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0647_MARRYMORE_SANCTUARY_CANDLE_1, timer_var=TIMER_701C
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        Return(),
    ]
)
