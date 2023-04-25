"""Script snippets that can be inserted easily."""

from typing import List

from randomizer.types.overworld_scripts.action_scripts.classes import (
    ActionScriptCommand,
)
from randomizer.types.overworld_scripts.action_scripts.commands.commands import (
    FaceSouthwest,
    Pause,
    SetWalkingSpeed,
    ShiftZDownPixels,
    ShiftZUpPixels,
    ShiftZUpSteps,
    VisibilityOn,
)
from randomizer.types.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
    VERY_FAST,
)

commands: List[ActionScriptCommand] = [
    FaceSouthwest(),
    VisibilityOn(),
    Pause(35),
    SetWalkingSpeed(VERY_FAST),
    ShiftZUpSteps(2),
    SetWalkingSpeed(FAST),
    ShiftZDownPixels(6),
    ShiftZUpPixels(6),
    ShiftZDownPixels(4),
    ShiftZUpPixels(4),
    ShiftZDownPixels(2),
    ShiftZUpPixels(2),
    Pause(20),
]
