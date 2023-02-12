#A0165_FALL_OFF_SPINNING_FLOWER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	PlaySound(sound=SO012_DIZZINESS, channel=4),
	SequencePlaybackOff(),
	SetWalkingSpeed(VERY_SLOW),
	Walk1StepSoutheast(),
	Return()
])
