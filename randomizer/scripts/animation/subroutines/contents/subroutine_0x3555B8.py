# pylint: disable=C0301,C0103

"""referenced by monster_spells MeteorBlast"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=29,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3555b8"),
        NewEffectObject(effect=EF0005_METEOR_BLAST, looping_on=True),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        FadeOutObject(duration=2),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        Layer3Off(prop=OVERLAP_ALL, bpp4=True),
        Pause2Frames(),
        ClearEffectIndex(),
        Jmp(["command_0x35252f"]),
    ])
