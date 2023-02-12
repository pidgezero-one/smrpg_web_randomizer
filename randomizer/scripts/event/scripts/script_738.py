# E0738_NIMBUS_LAND_FINAL_BOSS_FIGHT_TOWN_SQUARE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(LAYER_3, A0808_NIMBUS_EXTERIOR_LAYER_3),
        SetTempSyncActionScript(NPC_0, A0803_INC_PALETTE_ROW),
        SetTempSyncActionScript(NPC_2, A0807_INC_PALETTE_ROW_2),
        SetTempSyncActionScript(NPC_6, A0803_INC_PALETTE_ROW),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthSteps(3),
                ASShiftNortheastSteps(6),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=11, y=59, z=2, direction=EAST),
                ASFloatingOff(),
                ASFaceNortheast(),
                ASVisibilityOff(),
            ],
        ),
        RunEventAsSubroutine(
            E0822_NIMBUS_LAND_OCCUPIED_EXTERIOR_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=True, duration=60),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(NORMAL), ASShiftNortheastSteps(5)],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASShiftNortheastSteps(2),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(NORMAL),
                ASWalk1StepNortheast(),
                ASSetWalkingSpeed(SLOW),
                ASShiftNortheastPixels(8),
                ASSetSequenceSpeed(NORMAL),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftNortheastPixels(8),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASPause(1),
                ASFixedFCoordOn(),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASShiftSoutheastSteps(2),
                ASSetSequenceSpeed(SLOW),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueAsync(target=NPC_8, subscript=[ASPause(1), ASFaceSoutheast()]),
        Pause(10),
        RememberLastObject(),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASFaceNortheast(),
                ASPause(1),
                ASSetAllSpeeds(NORMAL),
                ASShiftNortheastSteps(3),
                ASSetWalkingSpeed(SLOW),
                ASShiftNorthwestSteps(2),
                ASFaceNortheast(),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(1),
                ASSetSequenceSpeed(FAST),
                ASShiftSoutheastSteps(4),
                ASSetAllSpeeds(NORMAL),
                ASShiftNortheastSteps(2),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPause(1),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(NORMAL),
                ASWalk1StepSoutheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFaceNorthwest(),
                ASPause(1),
                ASSetAllSpeeds(NORMAL),
                ASShiftNorthwestSteps(2),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASFaceNorthwest(),
                ASPause(1),
                ASWalk1StepNortheast(),
                ASShiftNorthwestSteps(4),
            ],
        ),
        RememberLastObject(),
        Pause(1),
        SetSyncActionScript(NPC_0, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        PauseActionScript(NPC_0),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_738_action_queue_async_23_SUBSCRIPT_pause_3"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_738_action_queue_async_23_SUBSCRIPT_pause_3"]
                ),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        Pause(1),
        ActionQueueSync(target=NPC_9, subscript=[ASPause(1), ASFaceSouthwest()]),
        SetSyncActionScript(NPC_7, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        Pause(1),
        PauseActionScript(NPC_7),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_738_action_queue_async_30_SUBSCRIPT_pause_3"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_738_action_queue_async_30_SUBSCRIPT_pause_3"]
                ),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        Pause(1),
        ActionQueueSync(target=NPC_9, subscript=[ASPause(1), ASFaceSoutheast()]),
        SetSyncActionScript(NPC_4, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        Pause(1),
        PauseActionScript(NPC_4),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_738_action_queue_async_37_SUBSCRIPT_pause_3"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_738_action_queue_async_37_SUBSCRIPT_pause_3"]
                ),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASPause(10),
                ASFaceNorthwest(),
                ASPause(10),
                ASFaceSouthwest(),
                ASPause(10),
                ASFaceNortheast(),
                ASPause(10),
                ASFaceSoutheast(),
                ASPause(10),
                ASFaceNorthwest(),
                ASPause(10),
                ASFaceNortheast(),
                ASPause(5),
                ASFaceSouthwest(),
                ASPause(5),
                ASFaceNortheast(),
                ASPause(5),
                ASFaceSoutheast(),
                ASPause(5),
                ASFaceNorthwest(),
                ASPause(5),
                ASFaceNortheast(),
                ASPause(3),
                ASFaceSouthwest(),
                ASPause(2),
                ASFaceNorthwest(),
                ASPause(2),
                ASFaceNortheast(),
                ASPause(2),
                ASFaceSouthwest(),
                ASPause(2),
                ASFaceSoutheast(),
                ASPause(2),
                ASFaceNortheast(),
                ASSetWalkingSpeed(VERY_FAST),
                ASFixedFCoordOn(),
                ASShiftNortheastPixels(2),
                ASStartLoopNTimes(9),
                ASShiftSouthwestPixels(4),
                ASShiftNortheastPixels(4),
                ASEndLoop(),
            ],
        ),
        SetSyncActionScript(NPC_8, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        Pause(1),
        CloseDialog(),
        SetSyncActionScript(NPC_7, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        Pause(1),
        CloseDialog(),
        SetSyncActionScript(NPC_4, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        SetSyncActionScript(NPC_0, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        SetSyncActionScript(NPC_2, A0880_CROWD_AROUND_NIMBUS_BOSS),
        Pause(1),
        Pause(1),
        CloseDialog(),
        Pause(1),
        Pause(1),
        CloseDialog(),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSequencePlaybackOff(),
                ASAddZCoord1Step(),
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpPixels(8),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftZUpPixels(4),
                ASSetWalkingSpeed(VERY_FAST),
                ASDecZCoord1Step(),
                ASShiftZDownPixels(12),
                ASPlaySound(sound=SO020_LIGHTING_BOLT, channel=4),
                ASSequencePlaybackOn(),
            ],
        ),
        PauseActionScript(NPC_0),
        PauseActionScript(NPC_4),
        PauseActionScript(NPC_7),
        PauseActionScript(NPC_8),
        PauseActionScript(NPC_2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASJumpToHeight(height=112, silent=True),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASShiftNortheastSteps(2),
                ASShiftNortheastPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASJumpToHeight(height=112, silent=True),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASShiftSouthwestSteps(2),
                ASShiftSouthwestPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASJumpToHeight(height=112, silent=True),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASShiftSoutheastSteps(2),
                ASShiftSoutheastPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASJumpToHeight(height=112, silent=True),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASSetWalkingSpeed(NORMAL),
                ASShiftSouthSteps(2),
                ASShiftSouthPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASJumpToHeight(height=112, silent=True),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASSetWalkingSpeed(NORMAL),
                ASShiftNorthwestSteps(2),
                ASShiftNorthwestPixels(4),
            ],
        ),
        RememberLastObject(),
        Pause(1),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASFaceSoutheast(),
                ASPause(10),
                ASFaceNorthwest(),
                ASPause(10),
                ASFaceSouthwest(),
                ASPause(10),
                ASFaceNortheast(),
            ],
        ),
        Pause(1),
        Pause(1),
        FreezeCamera(),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASFaceSoutheast(),
                ASPause(2),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASSequenceLoopingOn(),
                ASShiftSouthPixels(12),
                ASSequenceLoopingOff(),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalk1StepSouthwest()],
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASFixedFCoordOff(), ASPause(1), ASFaceSouthwest()]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASFixedFCoordOff(), ASPause(1), ASFaceSouthwest()]
        ),
        ActionQueueSync(
            target=NPC_7, subscript=[ASFixedFCoordOff(), ASPause(1), ASFaceSouthwest()]
        ),
        ActionQueueSync(
            target=NPC_8, subscript=[ASFixedFCoordOff(), ASPause(1), ASFaceSouthwest()]
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASVisibilityOn(),
                ASJumpToHeight(160),
                ASShiftNortheastPixels(1),
                ASFloatingOn(),
                ASShiftNortheastSteps(4),
                ASShiftNortheastPixels(11),
            ],
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASShiftNortheastSteps(2),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(1),
                ASResetProperties(),
            ],
        ),
        Pause(1),
        ActionQueueSync(
            target=NPC_9, subscript=[ASFaceSoutheast(), ASPause(2), ASFaceNortheast()]
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASPause(4), ASFaceSoutheast(), ASPause(2), ASFaceNortheast()],
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASPause(4), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASPause(4), ASFaceNorthwest(), ASPause(2), ASFaceNortheast()],
        ),
        ActionQueueSync(target=NPC_8, subscript=[ASPause(4), ASFaceSoutheast()]),
        Pause(1),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASFaceSoutheast(), ASPause(2), ASFaceSouthwest()]
        ),
        Pause(1),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASFaceSoutheast(), ASPause(2), ASFaceNortheast()]
        ),
        Pause(1),
        Pause(1),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASFaceSoutheast(), ASPause(2), ASFaceSouthwest()]
        ),
        Pause(1),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASShiftNortheastSteps(3),
                ASTransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
                ASStartLoopNTimes(1),
                ASSetSpriteSequence(
                    index=10,
                    sprite_offset=4,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=11,
                    sprite_offset=4,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(4),
                ASEndLoop(),
                ASSetSpriteSequence(
                    index=10,
                    sprite_offset=4,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASFaceSouthwest(), ASPause(30), ASFaceSoutheast()]
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASPause(50), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_7, subscript=[ASFaceSouthwest(), ASPause(20), ASFaceNorthwest()]
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASSequenceLoopingOff(), ASSequencePlaybackOff()]
        ),
        ClearBit(NIMBUS_BOSS_IN_TOWN_SQUARE),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetVarToConst(TEMP_70A9, 29),
        SetBit(TEMP_704A_2),
        RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpIfBitClear(STATUE_KEEPER_FIGHT_PRESENT, ["EVENT_738_enter_area_0"]),
        SummonObjectToSpecificLevel(
            NPC_2, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT
        ),
        EnterArea(
            room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
            face_direction=SOUTH,
            x=15,
            y=46,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_738_enter_area_0",
        ),
        RunEventAsSubroutine(E3660_NIMBUS_REPOPULATE_CASTLE_UPON_LIBERATION),
        FadeInFromBlack(sync=True),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
