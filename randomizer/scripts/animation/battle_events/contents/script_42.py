"""BE0042_BB_BOMBS_EXPLODE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3accff"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3acd32"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3acd61"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3acd90"], bit_2=True, bit_4=True
        ),
        Pause1Frame(),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3acdbf"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=0,
            destinations=["queuestart_0x3acddd"],
            character_slot=True,
            bit_4=True,
        ),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3acddd"],
            character_slot=True,
            bit_4=True,
        ),
        SpriteQueue(
            field_object=2,
            destinations=["queuestart_0x3acddd"],
            character_slot=True,
            bit_4=True,
        ),
        RunSubroutine(["command_0x3a7734"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
        RunSubroutine(["command_0x3a756c"]),
        RunSubroutine(["command_0x3a8698"]),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)
