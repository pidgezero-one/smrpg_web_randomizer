"""Int subclass instances representing valid VRAM priority levels."""

from randomizer.types.overworld_scripts.action_scripts.constants.classes import (
    VRAMPriority,
)

MARIO_OVERLAPS_ON_ALL_SIDES = VRAMPriority(0)
NORMAL_PRIORITY = VRAMPriority(1)
OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES = VRAMPriority(2)
PRIORITY_3 = VRAMPriority(3)
