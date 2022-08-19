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
	SetPriority(2),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetAllSpeeds(speed=FASTER),
	TransferToXYZF(x=2, y=48, z=0, direction=EAST),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	SetVarToRandom(PRIMARY_TEMP_700C, 30),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	PlaySound(sound=S049_BIG_SHELL_HIT, channel=4),
	ShiftSouthwestPixels(8),
	JmpIfObjectWithinRange(object=NPC_4, usually=0, tiles=3, destinations=["ACTION_709_set_bit_18"], identifier="ACTION_709_db_14"),
	JumpToHeight(24),
	Walk1StepSoutheast(),
	Jmp(["ACTION_709_db_14"]),
	SetBit(TEMP_7043_1, identifier="ACTION_709_set_bit_18"),
	Jmp(["ACTION_708_jump_to_height_20"])
])
