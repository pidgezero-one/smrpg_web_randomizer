"""NokNokShell miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0059_SUPER_JUMP_HIT_3), Jmp(["command_0x358251"])]
)
