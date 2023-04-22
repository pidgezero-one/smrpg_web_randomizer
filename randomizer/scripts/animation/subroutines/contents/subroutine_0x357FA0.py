# pylint: disable=C0301,C0103

"""referenced by monster_attacks Howl, monster_attacks ScrowBell, monster_attacks FunRun, monster_attacks Stench, monster_attacks ViroPlasm, monster_attacks Sporocyst"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=66,
    script=[
        ResetTargetMappingMemory(identifier="command_0x357fa0"),
        ResetObjectMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=8,
            y=-20,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=256, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        ResetTargetMappingMemory(identifier="command_0x357fb6"),
        ResetObjectMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=0,
            y=0,
            z=-16,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=256, arch_height=48),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        ResetTargetMappingMemory(identifier="command_0x357fcc"),
        ResetObjectMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        SetAMEM40ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=8,
            y=-16,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=96),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
    ],
)
