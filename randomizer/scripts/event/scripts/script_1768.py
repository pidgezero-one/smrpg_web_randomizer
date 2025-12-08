# pylint: disable=C0301

"""E1768_TEMPLE_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RemoveObjectFromCurrentLevel(NPC_1),
        RestoreAllHP(),
        RestoreAllFP(),
        FadeInFromBlack(sync=False),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_0),
        StartLoopNTimes(2),
        Pause(1, identifier="EVENT_1768_pause_242"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1768_pause_242"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        EndLoop(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ]),
        RemoveObjectFromSpecificLevel(
            NPC_1, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        SummonObjectToSpecificLevel(NPC_4, R324_MONSTRO_TOWN_OUTSIDE),
        SetBit(TEMPLE_BOSS_DEFEATED),
        SetBit(MELODY_BAY_SONG_3_UNLOCKED),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
    ]
)
