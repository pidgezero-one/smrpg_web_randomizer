"""HandCannon miss animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [PlaySound(sound=S0113_GENO_FINGER_SHOT_HIT), Jmp(["command_0x358251"])]
)
