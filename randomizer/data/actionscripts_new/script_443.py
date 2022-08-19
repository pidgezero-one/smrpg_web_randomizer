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
	SetPriority(3),
	SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	ShadowOff(),
	FaceMario(identifier="ACTION_443_face_mario_4"),
	StartLoopNTimes(7),
	Set700CToPressedButton(),
	Dec(PRIMARY_TEMP_700C),
	Dec(PRIMARY_TEMP_700C),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	Db(bytearray(b'\xc8\x11')),
	AddConstToVar(Z_COORD_2, 192),
	AddConstToVar(X_COORD_2, 64),
	AddConstToVar(Y_COORD_2, 48),
	TransferTo70167018701A(),
	EndLoop(),
	Jmp(["ACTION_443_face_mario_4"])
])
