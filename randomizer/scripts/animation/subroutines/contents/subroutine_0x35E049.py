# pylint: disable=C0301,C0103

"""referenced by items RockCandy"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=51,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35e049",
        ),
        NewEffectObject(effect=EF0005_METEOR_BLAST, looping_on=True),
        Db(bytearray(b"\x8a\x02")),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        MoveObject(
            speed=33,
            start_position=512,
            end_position=1024,
            apply_to_x=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
        ),
        MoveObject(
            speed=17,
            start_position=-257,
            end_position=-513,
            apply_to_y=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
        ),
        PlaySound(sound=S0105_ROCK_CANDY),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=120),
        ResetObjectMappingMemory(),
        Layer3Off(prop=OVERLAP_ALL, bpp4=True),
        Pause2Frames(),
        ClearEffectIndex(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
    ],
)
