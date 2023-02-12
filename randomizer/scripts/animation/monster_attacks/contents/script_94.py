# PhysicalAttack108

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357f07"]),
	RunSubroutine(["command_0x353140"]),
	RunSubroutine(["command_0x3523c4"]),
	RunSubroutine(["command_0x3577f2"]),
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=183, y=175, z=-48, set_x=True, set_y=True, set_z=True),
	ReturnSubroutine()
])
