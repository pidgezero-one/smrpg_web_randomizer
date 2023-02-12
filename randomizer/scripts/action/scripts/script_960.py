#A0960_FACTORY_2ND_BOSS_HENCHMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(NORMAL),
	JumpToHeight(80),
	Walk1StepSoutheast(),
	Return()
])
