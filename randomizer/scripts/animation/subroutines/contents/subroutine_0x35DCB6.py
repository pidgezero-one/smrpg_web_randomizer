# pylint: disable=C0301,C0103

"""referenced by items IceBomb"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=31,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35dcb6"),
        NewEffectObject(
            effect=EF0060_ICE_BOMB_SOLIDIFY_BG__BLUE_FREEZE_, looping_off=True
        ),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        PlaySound(sound=S0174_SOLIDIFY),
        PauseScriptUntil(condition=SEQ_4BPP_COMPLETE),
        Layer3Off(prop=OVERLAP_ALL, bpp4=True),
        Pause2Frames(),
        ClearEffectIndex(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
    ])
