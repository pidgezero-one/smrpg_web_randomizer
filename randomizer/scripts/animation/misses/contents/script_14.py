"""SuperHammer miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0054_HAMMER_HIT_1), Jmp(["command_0x358251"])]
)
