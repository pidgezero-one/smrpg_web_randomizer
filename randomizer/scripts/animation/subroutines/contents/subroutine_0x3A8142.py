# referenced by 

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 20, script = [
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=56, y=152, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=72, y=160, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
