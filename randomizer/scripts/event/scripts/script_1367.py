# pylint: disable=C0301

"""E1367_CURTAIN_GAME_SUCCESS_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_1, identifier="EVENT_1367_pause_action_script_0"),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        Pause(10),
        ActionQueueSync(
            target=NPC_1, subscript=[ASDb(bytearray(b"\xfd\x9ck")), ASFaceNorthwest()]
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNorthwestSteps(4),
                ASWalkNortheastSteps(2),
                ASWalkNortheastPixels(8),
                ASWalkNorthwestSteps(1),
                ASPause(15),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        Pause(20),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=35),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43),
        StartLoopNTimes(49),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=32),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=40),
        Pause(3),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ck")),
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNortheastSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNortheastSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNortheastSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        Pause(20),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43),
        StartLoopNTimes(39),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=44),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=40),
        Pause(3),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ck")),
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        Pause(20),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=35),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43),
        StartLoopNTimes(29),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=44),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=32),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=40),
        Pause(3),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ck")),
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                )
            ]),
        Pause(20),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=35),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        StartLoopNTimes(29),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=44),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=32),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36),
        Pause(3),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ck")),
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASFaceNorthwest(),
                ASPause(20),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASResetProperties(), ASFixedFCoordOff(), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASFixedFCoordOn(),
                ASDb(bytearray(b"\xfd\x9ck")),
                ASWalkNortheastSteps(2),
                ASPause(5),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASFixedFCoordOn(),
                ASWalkNortheastSteps(2),
                ASPause(5),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASFixedFCoordOn(),
                ASWalkNortheastSteps(2),
                ASPause(5),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        Pause(20),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47),
        StartLoopNTimes(9),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=43),
        StartLoopNTimes(9),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        StartLoopNTimes(29),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_1, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0577_CURTAIN_GAME_OPEN_CURTAIN),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=42),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=41),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=44),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=40),
        Pause(3),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ck")),
                ASResetProperties(),
                ASPause(40),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(2),
                ASWalkNortheastSteps(4),
                ASWalkNorthwestSteps(1),
                ASWalkSouthwestSteps(4),
                ASWalkNorthwestSteps(1),
                ASFaceNorthwest(),
                ASPause(30),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASResetProperties(),
                ASPause(40),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSouthwestSteps(4),
                ASWalkNortheastSteps(4),
                ASWalkSoutheastSteps(1),
                ASWalkNortheastSteps(1),
                ASWalkNorthwestSteps(1),
                ASFixedFCoordOn(),
                ASWalkNortheastSteps(1),
                ASFaceNorthwest(),
                ASFixedFCoordOff(),
                ASPause(30),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASResetProperties(),
                ASPause(40),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(3),
                ASJumpToHeight(112),
                ASWalkSouthwestSteps(6),
                ASWalkNorthwestSteps(3),
                ASFaceNorthwest(),
                ASPause(30),
                ASSetSpriteSequence(
                    index=6, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        Pause(20),
        SetSyncActionScript(NPC_1, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_2, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        SetSyncActionScript(NPC_3, A0576_CURTAIN_GAME_OPEN_CURTAIN),
        PlaySound(sound=SO090_CURTAIN, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=45),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=33),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=46),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=34),
        Pause(3),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=47),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=35),
        StartLoopNTimes(39),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1367_stop_music_FDA2_273"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1367_stop_music_FDA2_273"]),
        Pause(1),
        EndLoop(),
        EnableControlsUntilReturn([]),
        Jmp(["EVENT_1368_stop_music_FDA2_0"]),
        StopMusicFDA2(identifier="EVENT_1367_stop_music_FDA2_273"),
        MoveScriptToMainThread(),
        EnableControlsUntilReturn([]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(1),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastSteps(2),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastSteps(2),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastSteps(2),
            ]),
        Pause(30),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOff(),
                ASFaceNorthwest(),
                ASPause(10),
                ASJumpToHeight(50),
            ]),
        Jmp(["EVENT_1370_play_sound____"]),
    ]
)
