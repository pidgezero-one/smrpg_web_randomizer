# pylint: disable=C0301

"""E1368_CURTAIN_GAME_SUCCESS_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopMusicFDA2(identifier="EVENT_1368_stop_music_FDA2_0"),
        EnableControlsUntilReturn([]),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceSoutheast()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_1, subscript=[ASPause(10), ASFaceNortheast()]),
        ActionQueueSync(target=NPC_2, subscript=[ASPause(10), ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_3, subscript=[ASPause(10), ASFaceNortheast()]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASResetProperties(),
                ASFaceNorthwest(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkSouthwestPixels(8),
                ASWalkNorthwestSteps(2),
                ASWalkNorthwestPixels(13),
                ASPause(15),
                ASSetSpriteSequence(index=14, is_sequence=True, looping=True),
                ASPause(7),
                ASSetSpriteSequence(index=15, is_sequence=True, looping=True),
            ]),
        PlayMusicAtDefaultVolume(M32_AND_MY_NAMES_BOOSTER),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        PlaySound(sound=SO090_CURTAIN, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43),
        Pause(5),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=16,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(25),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASSequenceLoopingOn(),
                ASFixedFCoordOn(),
                ASJumpToHeight(112),
                ASWalkSoutheastSteps(3),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(target=NPC_1, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_2, subscript=[ASFaceSoutheast()]),
        ActionQueueAsync(target=NPC_3, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(5),
                ASWalkNortheastSteps(2),
                ASWalkNortheastPixels(8),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(3),
                ASWalkSouthwestPixels(8),
                ASWalkSoutheastSteps(2),
                ASFaceNorthwest(),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(5),
                ASWalkNortheastSteps(2),
                ASFaceNorthwest(),
            ]),
        Pause(10),
        ActionQueueAsync(
            target=MARIO, subscript=[ASResetProperties(), ASFaceSoutheast()]
        ),
        Pause(20),
        ActionQueueSync(target=NPC_1, subscript=[ASJumpToHeight(80), ASPause(20)]),
        ActionQueueSync(target=NPC_2, subscript=[ASJumpToHeight(80), ASPause(20)]),
        ActionQueueAsync(target=NPC_3, subscript=[ASJumpToHeight(80), ASPause(20)]),
        Pause(1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(FAST),
                ASBounceToXYWithHeight(x=3, y=20, height=0),
                ASFaceNorth(),
                ASPause(80),
                ASFaceEast(),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSequenceLoopingOff(), ASResetProperties(), ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASFixedFCoordOff(), ASFaceSoutheast()]
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASWalkNorthwestSteps(2),
                ASWalkSouthwestPixels(6),
                ASPause(30),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(SLOW),
                ASPause(25),
                ASSequenceLoopingOff(),
                ASPause(10),
                ASSetSequenceSpeed(FAST),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASPause(30),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(30),
                ASResetProperties(),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASWalkNortheastPixels(6),
                ASWalkSoutheastSteps(2),
                ASFaceNorthwest(),
            ]),
        Pause(1),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(60),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(
                    index=13, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        SetSyncActionScript(NPC_1, A0579_CURTAIN_GAME_HENCHMAN_SPIN),
        SetSyncActionScript(NPC_2, A0580_CURTAIN_GAME_HENCHMAN_SPIN),
        SetSyncActionScript(NPC_3, A0578_CURTAIN_GAME_HENCHMAN_SPIN),
        Pause(60),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASBounceToXYWithHeight(x=3, y=16, height=0),
                ASWalkNortheastPixels(8),
                ASFaceSoutheast(),
            ]),
        Pause(1),
        Set7000ToTappedButton(identifier="EVENT_1368_set_7000_to_tapped_button_49"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_1368_action_queue_sync_54"]
        ),
        Jmp(["EVENT_1368_set_7000_to_tapped_button_49"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(112),
                ASPause(60),
                ASSetSequenceSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetPriority(2),
            ],
            identifier="EVENT_1368_action_queue_sync_54"),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASPause(8),
                ASSetWalkingSpeed(FAST),
                ASFloatingOn(),
                ASShadowOn(),
                ASJumpToHeight(height=64, silent=True),
                ASWalkSoutheastSteps(3),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(8),
                ASSetWalkingSpeed(FAST),
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=6),
                ASWalkNorthPixels(7),
                ASWalkSouthPixels(7),
                ASWalkNorthPixels(4),
                ASWalkSouthPixels(4),
            ]),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASResetProperties(),
                ASFaceNorthwest(),
                ASPause(60),
                ASJumpToHeight(64),
                ASPause(30),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSequenceLoopingOff(), ASPause(30), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASSequenceLoopingOff(), ASPause(30), ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASSequenceLoopingOff(), ASPause(30), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASPlaySound(sound=SO024_TAPPING_FEET, channel=6),
                ASWalkNorthwestSteps(3),
            ]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASFixedFCoordOn(),
                ASPause(12),
                ASSetWalkingSpeed(VERY_FAST),
                ASJumpToHeight(32),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASWalkSouthwestSteps(2),
            ]),
        Pause(20),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Pause(45),
        ActionQueueAsync(target=NPC_0, subscript=[ASFaceSoutheast()]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkSoutheastSteps(3),
                ASWalkSoutheastPixels(8),
                ASWalkSouthwestSteps(6),
            ]),
        Pause(20),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(1),
                ASWalkNorthwestPixels(8),
                ASWalkSouthwestSteps(3),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(1),
                ASWalkNorthwestPixels(8),
                ASWalkSouthwestSteps(3),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASWalkNorthwestSteps(1),
                ASWalkNorthwestPixels(8),
                ASWalkSouthwestSteps(3),
            ]),
        Pause(45),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        Pause(20),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthwestPixels(10),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(3),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(3),
                ASVisibilityOff(),
                ASPause(45),
            ]),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=1),
        SetBit(CURTAIN_MINIGAME_COMPLETED),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        JmpIfBitSet(
            ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_1368_summon_to_level_145"]
        ),
        SetBit(TOWER_BOSS_1_STAR_PIECE),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
        SummonObjectToSpecificLevel(
            NPC_7,
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            identifier="EVENT_1368_summon_to_level_145"),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASVisibilityOn(),
                ASFaceNorthwest(),
                ASShiftToXYCoords(x=5, y=29),
            ]),
        Return(),
    ]
)
