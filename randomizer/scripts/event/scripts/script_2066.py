# pylint: disable=C0301

"""E2066_DOJO_BOSS_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2066_run_dialog_37"]),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["EVENT_2066_run_dialog_35"]),
        ActionQueueSync(
            target=NPC_1, subscript=[ASSetSequenceSpeed(NORMAL), ASFaceSouthwest()]
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
                ASWalkSouthwestSteps(1),
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
        RunEventAsSubroutine(E0861_DOJO_1ST_BOSS_CHALLENGE_SUBROUTINE),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpIfBitSet(GAME_OVER, ["EVENT_2066_fade_in_from_black_async_17"]),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2066_fade_in_from_black_async_17"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=6, y=8, z=3, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2066_fade_in_from_black_async_17"
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASPause(70),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASFixedFCoordOff(),
                ASPause(30),
                ASSetAllSpeeds(SLOW),
                ASWalkSouthwestSteps(1),
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
                ASWalkNortheastSteps(1),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        UnfreezeCamera(),
        Pause(30),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2066_stop_music_FDA2_24"]),
        JmpIfBitClear(GAME_OVER, ["EVENT_2066_jmp_30"]),
        StopMusicFDA2(identifier="EVENT_2066_stop_music_FDA2_24"),
        FadeOutMusicToVolume(duration=0, volume=100),
        PlayMusicAtDefaultVolume(M51_MONSTRO_TOWN),
        Return(),
        Jmp(["EVENT_2067_action_queue_async_0"], identifier="EVENT_2066_jmp_30"),
        Return(),
        RunDialog(
            dialog_id=DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2066_run_dialog_35",
        ),
        Return(),
        RunDialog(
            dialog_id=DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2066_run_dialog_37",
        ),
        Return(),
    ]
)
