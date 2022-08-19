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
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Pause(1, identifier="ACTION_609_pause_3"),
	JmpIfBitClear(TEMP_7044_7, ["ACTION_609_pause_3"]),
	ResetProperties(),
	FaceSouthwest(),
	SequenceLoopingOff(),
	SequencePlaybackOff(),
	TransferToObjectXY(NPC_1),
	TransferXYZFPixels(x=0, y=0, z=11, direction=EAST),
	SetWalkingSpeed(speed=FAST),
	VisibilityOn(),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	ShiftZUpPixels(1, identifier="ACTION_609_shift_z_up_pixels_14"),
	Pause(2),
	ShiftZDownPixels(1),
	Pause(2),
	JmpIfObjectInSpecificLevel(NPC_1, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, ["ACTION_609_shift_z_up_pixels_14"]),
	VisibilityOff(),
	Db(bytearray(b'\xfd\xf2')),
	Return()
])
