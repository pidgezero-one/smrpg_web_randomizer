# E2077_DOJO_BOSS_4

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2077_run_dialog_97"]),
        ActionQueueSync(
            target=NPC_3, subscript=[ASSetSequenceSpeed(NORMAL), ASFaceSouthwest()]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=5, y=16),
                ASFaceNortheast(),
            ],
        ),
        Pause(30),
        FreezeCamera(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=53, silent=True),
                ASShiftSouthwestSteps(1),
                ASPause(20),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=2, sprite_offset=4, is_sequence=True, looping=False
                ),
                ASPlaySound(sound=SO096_SWINGING_FIST, channel=6),
                ASPause(15),
                ASPlaySound(sound=SO096_SWINGING_FIST, channel=6),
                ASPause(30),
            ],
        ),
        RunEventAsSubroutine(E0866_DOJO_4TH_BOSS_CHALLENGE_SUBROUTINE),
        SetVarToConst(PRIMARY_TEMP_7000, 517),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        RestoreAllHP(),
        RestoreAllFP(),
        Pause(1),
        StopMusicFDA2(),
        FadeOutMusicToVolume(duration=0, volume=100),
        PlayMusicAtDefaultVolume(M51_MONSTRO_TOWN),
        Pause(1),
        FadeInFromBlack(sync=False),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPause(70),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASFixedFCoordOff(),
                ASPause(30),
                ASSetAllSpeeds(SLOW),
                ASShiftSouthwestSteps(1),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(70),
                ASResetProperties(),
                ASFaceNortheast(),
                ASFixedFCoordOff(),
                ASPause(30),
                ASSetAllSpeeds(SLOW),
                ASShiftNortheastSteps(1),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        UnfreezeCamera(),
        Pause(30),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2077_ret_98"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_2077_ret_98"]),
        Pause(3),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASFixedFCoordOff(),
                ASShiftSoutheastSteps(1),
                ASShiftSouthwestSteps(4),
                ASShiftNorthwestSteps(1),
                ASShiftSouthwestSteps(1),
                ASVisibilityOff(),
                ASPlaySound(sound=SO016_OPEN_DOOR, channel=6),
                ASPause(1),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=6),
                ASPause(1),
                ASPlaySound(sound=SO058_INSERT, channel=6),
                ASPause(1),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(8),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(8),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(1),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(8),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(8),
                ASPlaySound(sound=SO025_HEEL_CLICK, channel=6),
                ASPause(1),
                ASPlaySound(sound=SO016_OPEN_DOOR, channel=6),
                ASVisibilityOn(),
                ASShiftNortheastSteps(1),
                ASShiftSoutheastSteps(1),
                ASWalkToXYCoords(x=6, y=16),
                ASStopSound(),
                ASFaceSouthwest(),
            ],
        ),
        Pause(1),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASFixedFCoordOn(),
                ASShadowOff(),
                ASStopSound(),
                ASStopSound(),
                ASShadowOn(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=5, y=14),
                ASFaceSouthwest(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        Pause(1),
        Pause(1),
        SetSyncActionScript(NPC_3, A1006_DOJO_PERMA_JUMP),
        SetSyncActionScript(NPC_1, A1006_DOJO_PERMA_JUMP),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=32
        ),
        SetBit(DOJO_BOSS_4_DEFEATED),
        SetVarToConst(PRIMARY_TEMP_7000, 517),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        SetVarToConst(PRIMARY_TEMP_7000, 517),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(),
        RunDialog(
            dialog_id=DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2077_run_dialog_97",
        ),
        Return(identifier="EVENT_2077_ret_98"),
    ]
)
