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
	FloatingOff(),
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetWalkingSpeed(speed=FAST),
	SetPriority(2),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	VarShiftLeft(PRIMARY_TEMP_700C, 255),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(23),
	EndLoop(),
	FloatingOn(identifier="ACTION_286_floating_on_11"),
	JumpToHeight(height=0, silent=True),
	Pause(1, identifier="ACTION_286_pause_13"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_286_pause_13"]),
	ShadowOff(),
	PlaySound(sound=S073_THWOMP_STOMP, channel=4),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	SetMem704XAt700CBit(),
	Pause(20),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	ClearMem704XAt700CBit(),
	ShadowOn(),
	SetWalkingSpeed(speed=VERY_FAST, identifier="ACTION_286_set_animation_speed_25"),
	ShiftZUpPixels(2),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Z, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_286_set_animation_speed_25"]),
	Pause(110),
	Jmp(["ACTION_286_floating_on_11"])
])
