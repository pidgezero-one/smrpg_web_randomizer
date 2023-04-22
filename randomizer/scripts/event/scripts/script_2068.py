# pylint: disable=C0301

"""E2068_DOJO_BOSS_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0, subscript=[ASSetSequenceSpeed(NORMAL), ASFaceSouthwest()]
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
        RunEventAsSubroutine(E0862_DOJO_2ND_BOSS_CHALLENGE_SUBROUTINE),
        SetVarToConst(PRIMARY_TEMP_7000, 515),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        RestoreAllHP(),
        RestoreAllFP(),
        Pause(1),
        StopMusicFDA2(),
        FadeOutMusicToVolume(duration=0, volume=100),
        PlayMusicAtDefaultVolume(M51_MONSTRO_TOWN),
        Pause(1),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2068_fade_in_from_black_async_60"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_2068_fade_in_from_black_async_60"]),
        SetBit(DOJO_BOSS_2_DEFEATED),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromSpecificLevel(NPC_0, R255_MONSTRO_TOWN_JINXS_DOJO),
        SummonObjectToCurrentLevel(NPC_2),
        SummonObjectToSpecificLevel(NPC_2, R255_MONSTRO_TOWN_JINXS_DOJO),
        RunEventAsSubroutine(E0863_DOJO_2ND_BOSS_CHALLENGE_DEESCALATE),
        FadeInFromBlack(sync=False),
        ActionQueueSync(
            target=NPC_2,
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
        Jmp(["EVENT_2068_action_queue_async_62"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2068_fade_in_from_black_async_60"
        ),
        ActionQueueSync(
            target=NPC_0,
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
            identifier="EVENT_2068_action_queue_async_62",
        ),
        UnfreezeCamera(),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2068_pause_64"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_2068_pause_64"]),
        SetVarToConst(PRIMARY_TEMP_7000, 515),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Pause(30, identifier="EVENT_2068_pause_64"),
        Return(),
    ]
)
