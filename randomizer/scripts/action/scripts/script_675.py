"""A0675_ROSE_TOWN_LIBERATED_WATER_KID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(32),
        JmpToSubroutine(["ACTION_672_visibility_off_10"]),
        Walk1StepSouthwest(),
        FaceNorthwest(),
        Pause(160),
        Walk1StepNortheast(),
        JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
        Return(),
    ]
)
