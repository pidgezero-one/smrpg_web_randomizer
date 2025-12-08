# pylint: disable=C0301

"""E2209_KEEP_1ST_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(30, identifier="EVENT_2209_pause_0"),
        FadeOutMusicToVolume(duration=7, volume=0),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTER), ASWalkNortheastSteps(4)]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=25, y=101),
                ASFaceSouthwest(),
                ASPlaySound(sound=SO044_GHOST_FLOAT, channel=4),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(2),
                ASEndLoop(),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
                ASVisibilityOn(),
            ]),
        Pause(15),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=False),
            ]),
        Pause(80),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2209_fade_in_from_black_async_10"]),
        ResetAndChooseGame(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2209_fade_in_from_black_async_10"
        ),
        PlayMusicAtDefaultVolume(M51_MONSTRO_TOWN),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=138, row=11),
        RunEventAsSubroutine(E0942_KEEP_FIRST_BOSS_SUMMON_CHEST),
        PaletteSet(palette_set=139, row=1),
        SetSyncActionScript(NPC_0, A0014_FLOATING_CHEST),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(2),
                ASEndLoop(),
                ASStartLoopNTimes(1),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
                ASVisibilityOn(),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASResetProperties(), ASFaceSouthwest(), ASSequenceLoopingOn()]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkNorthwestSteps(3),
                ASFaceSoutheast(),
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
            ]),
        SetBit(KEEP_BOSS_1_DEFEATED),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
