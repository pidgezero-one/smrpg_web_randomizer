"""A0376_TURN_RANDOMLY_IN_PLACE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        TurnRandomDirection(identifier="ACTION_376_turn_random_direction_0"),
        Pause(16),
        TurnRandomDirection(),
        Pause(32),
        JmpIfRandom1of2(["ACTION_376_turn_random_direction_0"]),
        TurnRandomDirection(),
        Pause(48),
        Jmp(["ACTION_376_turn_random_direction_0"]),
    ]
)
