#A0387_JUMPING_TOWER_SPOOKUM

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(FAST),
	JumpToHeight(108),
	ShiftNortheastSteps(2),
	Return()
])
