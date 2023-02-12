# referenced by battle_events BE0007_COUNTDOWN_RUNS_SCHEDULE_1_00_3_00_5_00_6_00_7_00, battle_events BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 40, script = [
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=72, y=176, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=88, y=184, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=104, y=192, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=120, y=200, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
