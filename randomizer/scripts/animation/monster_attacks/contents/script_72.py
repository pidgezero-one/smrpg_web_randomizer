"""Pierce animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35788e"]),
        RunSubroutine(["command_0x35251b"]),
        PlaySound(sound=S0039_CLAW),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523ee"]),
        ReturnSubroutine(),
    ]
)
