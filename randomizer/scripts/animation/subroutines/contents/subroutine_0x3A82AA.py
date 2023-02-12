# referenced by battle_events BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC, battle_events BE0022_YARIDOVICH_MIRAGE_ATTACK

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 30, script = [
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=184, y=152, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=200, y=160, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=216, y=168, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
