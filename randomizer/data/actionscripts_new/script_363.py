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
	ClearSolidityBits(bit_7=True),
	SetWalkingSpeed(speed=FAST),
	ShiftSoutheastPixels(2, identifier="ACTION_363_shift_southeast_pixels_2"),
	JmpIfMarioInAir(["ACTION_363_clear_bit_5"]),
	Jmp(["ACTION_363_shift_southeast_pixels_2"]),
	ClearBit(TEMP_7044_7, identifier="ACTION_363_clear_bit_5"),
	ResetProperties(),
	FaceNorthwest(),
	SetAllSpeeds(speed=NORMAL),
	ShiftZDownPixels(1),
	SetSolidityBits(bit_7=True),
	Return()
])
