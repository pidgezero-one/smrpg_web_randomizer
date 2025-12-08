# pylint: disable=C0301

"""E0690_MARRYMORE_RED_TOAD_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_690_fade_out_music_FDA3_5"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_690_run_dialog_insert"]),
        RunDialog(
            dialog_id=DI2332_MARRYMORE_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2114_MARRYMORE_BOSS_NAMES,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_690_run_dialog_insert"),
        RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
        Return(),
        FadeOutMusicFDA3(identifier="EVENT_690_fade_out_music_FDA3_5"),
        ActionQueueAsync(target=MEM_70A8, subscript=[ASFaceNortheast()]),
        PlayMusicAtDefaultVolume(M49_CELEBRATIONAL),
        Pause(30),
        RunDialog(
            dialog_id=DI2331_MARRYMORE_COMPOSER,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        Pause(170),
        Pause(180),
        Pause(10),
        PlayMusicAtDefaultVolume(M39_MARRYMORE),
        CloseDialog(),
        Return(),
    ]
)
