"""RibbitStick miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0018_SUPER_JUMP_HIT_1), Jmp(["command_0x358251"])]
)
