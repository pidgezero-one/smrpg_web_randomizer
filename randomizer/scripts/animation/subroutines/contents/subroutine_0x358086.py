# referenced by ally_spells Come Back, ally_spells Geno Boost, ally_spells Shocker, ally_spells Poison Gas, ally_spells Terrorize, ally_spells Psychopath, ally_spells Therapy, ally_spells Thunderbolt, ally_spells Snowy, ally_spells Mute, ally_spells Star Rain, ally_spells Crusher, ally_spells Bowser Crush

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=23,
    script=[
        SpriteSequence(sequence=0, looping_off=True, identifier="command_0x358086"),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=12,
            y=-6,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=1664, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ResetTargetMappingMemory(),
        ReturnSubroutine(),
    ],
)
