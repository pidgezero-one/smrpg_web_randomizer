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
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	ShadowOn(),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	Db(bytearray(b'\xc8\x00')),
	AddConstToVar(X_COORD_2, 62976),
	AddConstToVar(Y_COORD_2, 1280),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	VisibilityOn(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=1, is_sequence=True),
	ShiftNortheastSteps(4),
	PlaySound(sound=S050_WATER_DROPLET, channel=4),
	Pause(1),
	ResetProperties(),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=FASTEST),
	SetSequenceSpeed(speed=FAST),
	AddZCoord1Step(),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZUpPixels(8),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(4),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(2),
	StartLoopNTimes(1),
	ShiftZDownPixels(2),
	ShiftZUpPixels(2),
	EndLoop(),
	SetWalkingSpeed(speed=FASTEST),
	ShiftNortheastPixels(4),
	ShiftZDownPixels(12),
	DecZCoord1Step(),
	VisibilityOff(),
	Return()
])
