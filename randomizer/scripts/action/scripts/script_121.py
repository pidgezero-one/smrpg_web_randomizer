#A0121_MK_BRANCH_HALLWAY_SPINNING_TOAD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TurnRandomDirection(identifier="ACTION_121_turn_random_direction_0"),
	Pause(4),
	TurnRandomDirection(),
	Pause(8),
	Jmp(["ACTION_121_turn_random_direction_0"])
])
