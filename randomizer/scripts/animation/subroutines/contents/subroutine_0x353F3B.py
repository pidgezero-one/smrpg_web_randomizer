# pylint: disable=C0301,C0103

"""referenced by monster_attacks InkBlast"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=48,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=-16,
            y=11,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x353f3b",
        ),
        Pause2Frames(),
        NewEffectObject(effect=EF0039_BLACK_BALL_ORB, playback_off=True),
        FadeInEffect(duration=1),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        PlaySound(sound=S0143_TOSS),
        ResetTargetMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=16,
            y=-8,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=512, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        PlaySound(sound=S0122_POISONED),
        Layer3Off(prop=OVERLAP_ALL, bpp4=True),
        Pause2Frames(),
        ClearEffectIndex(),
        Jmp(["command_0x35252f"]),
    ],
)
