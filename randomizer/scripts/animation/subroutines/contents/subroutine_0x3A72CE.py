# pylint: disable=C0301,C0103

"""referenced by battle_events BE0024_MACHINE_MADE_YARIDOVICH_MULTIPLIER, battle_events BE0069_AXEM_RANGERS_ARE_DEFEATED, battle_events BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE, battle_events BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS, battle_events BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER, battle_events BE0002_BELOME_SWALLOWS_MALLOW, battle_events BE0007_COUNTDOWN_RUNS_SCHEDULE_1_00_3_00_5_00_6_00_7_00, battle_events BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=90,
    script=[
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=2048, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=64, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=48),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=96),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=144),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=192),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=240),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=288),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ReturnSubroutine(),
    ])
