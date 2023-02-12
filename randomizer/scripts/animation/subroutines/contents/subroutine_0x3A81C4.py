# referenced by battle_events BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE, battle_events BE0032_BUNDT_MOVES_AGAIN_BOTH_COOKS_RUN_AWAY, battle_events BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 40, script = [
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=152, y=184, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=168, y=192, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=72, y=128, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine(),
	ResetTargetMappingMemory(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=88, y=136, z=0, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
