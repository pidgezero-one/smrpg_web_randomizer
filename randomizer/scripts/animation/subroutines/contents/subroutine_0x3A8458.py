# referenced by 

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 10, script = [
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=104, y=168, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
