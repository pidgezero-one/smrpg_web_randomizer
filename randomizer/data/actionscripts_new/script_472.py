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
	VisibilityOff(),
	Db(bytearray(b'\xfd\x12')),
	FaceNortheast(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65512),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	Pause(3, identifier="ACTION_472_pause_8"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=128, tiles=3, destinations=["ACTION_472_db_11"]),
	Jmp(["ACTION_472_pause_8"]),
	UnknownJmp3C(0x00, 0x40, ["ACTION_472_visibility_on_13"], identifier="ACTION_472_db_11"),
	Jmp(["ACTION_472_pause_8"]),
	VisibilityOn(identifier="ACTION_472_visibility_on_13"),
	SequenceLoopingOn(),
	SetSolidityBits(bit_4=True),
	SetSolidityBits(cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	PlaySound(sound=S030_SURPRISED_MONSTER, channel=4),
	SetAllSpeeds(speed=FASTER),
	JumpToHeight(108),
	ShiftNortheastSteps(3),
	Pause(15),
	FaceNorthwest(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	Walk1StepFDirection(identifier="ACTION_472_walk_1_step_f_direction_26"),
	Pause(15),
	TurnClockwise45DegreesNTimes(6),
	Pause(5),
	TurnClockwise45DegreesNTimes(6),
	Pause(15),
	Jmp(["ACTION_472_walk_1_step_f_direction_26"])
])
