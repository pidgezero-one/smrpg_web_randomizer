"""BE0056_SHY_AWAY_WATERS_SMILAX_PART_2"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 8),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a774a"]),
        ClearAMEM8Bit(0x67),
        SetAMEM8BitTo7E1x(0x67, 0x7EE00D),
        IncAMEM8BitByConst(0x67, 2),
        Set7E1xToAMEM8Bit(0x7EE00D, 0x67),
        RunSubroutine(["command_0x3a7734"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ad81b"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3ad835"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3ad84f"], bit_2=True, bit_4=True
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        RunSubroutine(["command_0x3a773f"]),
        Jmp(["command_0x3a7550"]),
    ]
)
