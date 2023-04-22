# pylint: disable=C0301,C0103

"""referenced by battle_events BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS, battle_events BE0002_BELOME_SWALLOWS_MALLOW"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=62,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1536, arch_height=80),
        PauseScriptUntil(condition=0x07),
        ResetObjectMappingMemory(),
        ResetSpriteSequence(),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1024, arch_height=0),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(index=6, target_address=0x3A8AC0),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        VisibilityOff(),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        ObjectQueueAtOffsetAndIndex(index=6, target_address=0x3A8AC0),
        VisibilityOn(),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ],
)
