"""BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ac063"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=5, destinations=["queuestart_0x3ac09f"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=6, destinations=["queuestart_0x3ac148"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2,
            destinations=["queuestart_0x3ac1f1"],
            character_slot=True,
            bit_4=True,
        ),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ac234"],
            character_slot=True,
            bit_4=True,
        ),
        SpriteQueue(
            field_object=0,
            destinations=["queuestart_0x3ac2c0"],
            character_slot=True,
            bit_4=True,
        ),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)
