# referenced by monster_attacks PhysicalAttack81

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 15, script = [
	SetAMEM60ToCurrentTarget(identifier="queuestart_0x356078"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	RunSubroutine(["command_0x35358a"]),
	RunSubroutine(["command_0x35253b"])
])
