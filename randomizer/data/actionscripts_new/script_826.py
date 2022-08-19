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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 473, ["ACTION_826_set_solidity_bits_61"]),
	Set700CToPressedButton(),
	CompareVarToConst(PRIMARY_TEMP_700C, 24),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_826_shift_f_direction_steps_55"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_826_shadow_on_34"]),
	ShadowOn(identifier="ACTION_826_shadow_on_7"),
	VisibilityOff(),
	FloatingOff(),
	SetSolidityBits(cant_pass_walls=True),
	Pause(20),
	TransferToXYZF(x=7, y=38, z=2, direction=SOUTHEAST),
	FaceSouthwest(),
	JumpToHeight(96),
	Pause(20),
	FloatingOn(),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(24),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Pause(30),
	JumpToHeight(64),
	Walk1StepSouthwest(),
	Pause(5),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Pause(58),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	JumpToHeight(96),
	ClearSolidityBits(cant_pass_walls=True),
	Walk1StepSoutheast(),
	ShadowOff(),
	Walk1StepSoutheast(),
	Jmp(["ACTION_826_shadow_on_7"]),
	ShadowOn(identifier="ACTION_826_shadow_on_34"),
	VisibilityOff(),
	FloatingOff(),
	SetSolidityBits(cant_pass_walls=True),
	Pause(20),
	TransferToXYZF(x=14, y=24, z=0, direction=SOUTHEAST),
	JumpToHeight(96),
	Pause(20),
	FloatingOn(),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(24),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Pause(42),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Pause(2),
	JumpToHeight(96),
	ClearSolidityBits(cant_pass_walls=True),
	ShadowOff(),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_826_shadow_on_34"]),
	ShiftFDirectionSteps(4, identifier="ACTION_826_shift_f_direction_steps_55"),
	Pause(8),
	TurnClockwise45DegreesNTimes(2),
	Pause(8),
	TurnClockwise45DegreesNTimes(2),
	Jmp(["ACTION_826_shift_f_direction_steps_55"]),
	SetSolidityBits(cant_pass_walls=True, identifier="ACTION_826_set_solidity_bits_61"),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(2),
	EndLoop(),
	SetWalkingSpeed(speed=NORMAL),
	FixedFCoordOn(),
	StartLoopNTimes(2, identifier="ACTION_826_start_loop_n_times_69"),
	Walk1StepSoutheast(),
	Pause(30),
	EndLoop(),
	StartLoopNTimes(2),
	Walk1StepNorthwest(),
	Pause(30),
	EndLoop(),
	Jmp(["ACTION_826_start_loop_n_times_69"])
])
