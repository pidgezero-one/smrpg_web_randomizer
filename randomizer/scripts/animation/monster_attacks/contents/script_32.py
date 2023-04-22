"""GunkBall animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x353437"]),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3536c4"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x352fa6"]),
        RunSubroutine(["command_0x357b73"]),
        SpriteSequence(sequence=4),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=30),
        SetAMEM16BitToConst(0x60, 4),
        RunSubroutine(["command_0x3524b1"]),
        PauseScriptUntilSpriteSequenceDone(),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x35336f"]),
        ReturnSubroutine(),
    ]
)
