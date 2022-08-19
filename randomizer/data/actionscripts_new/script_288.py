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
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	FloatingOn(),
	SequencePlaybackOn(),
	ResetProperties(),
	ShadowOn(),
	SetWalkingSpeed(speed=SLOW),
	JumpToHeight(108),
	ShiftFDirectionPixels(8),
	SetWalkingSpeed(speed=NORMAL),
	ShiftFDirectionPixels(4),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftFDirectionPixels(4),
	Pause(1, identifier="ACTION_288_pause_14"),
	JmpIfMarioInAir(["ACTION_288_pause_14"]),
	ClearBit(TEMP_7044_4),
	Return()
])
