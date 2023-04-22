"""HurlyGloves miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0159_BIG_DEEP_HIT), Jmp(["command_0x358251"])]
)
