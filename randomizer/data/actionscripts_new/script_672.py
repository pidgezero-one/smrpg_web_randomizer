#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(1),
	FaceSoutheast(),
	SequenceLoopingOff(),
	Pause(160),
	ShiftSoutheastSteps(1),
	ShiftNortheastSteps(1),
	JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	Return(),
	VisibilityOff(identifier="ACTION_672_visibility_off_10"),
	TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	FaceSoutheast(),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	VisibilityOn(),
	Walk1StepSoutheast(),
	SetSolidityBits(cant_walk_through=True),
	ShiftSoutheastSteps(4),
	SetSolidityBits(cant_pass_walls=True),
	FloatingOn(),
	ShiftSouthwestSteps(2),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	ShiftSouthwestSteps(2),
	Return(),
	ShiftNortheastSteps(2, identifier="ACTION_672_shift_northeast_steps_26"),
	ShiftNortheastPixels(8),
	SetSolidityBits(cant_pass_walls=True),
	FloatingOn(),
	ShiftNortheastSteps(1),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	ShiftNortheastPixels(8),
	ShiftNorthwestSteps(4),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Walk1StepNorthwest(),
	VisibilityOff(),
	TransferToXYZF(x=16, y=85, z=0, direction=EAST),
	Return()
])
