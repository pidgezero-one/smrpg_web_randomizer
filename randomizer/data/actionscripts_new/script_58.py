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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
	Set700CToPressedButton(),
	SetVarToConst(TEMP_702C, 20),
	DecVarFrom700C(TEMP_702C),
	Mem700CAndConst(0x0007),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_58_pause_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_58_pause_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_58_pause_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_58_pause_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_58_pause_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_58_pause_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_58_pause_21"]),
	Pause(1),
	Pause(1, identifier="ACTION_58_pause_15"),
	Pause(1, identifier="ACTION_58_pause_16"),
	Pause(1, identifier="ACTION_58_pause_17"),
	Pause(1, identifier="ACTION_58_pause_18"),
	Pause(1, identifier="ACTION_58_pause_19"),
	Pause(1, identifier="ACTION_58_pause_20"),
	Pause(1, identifier="ACTION_58_pause_21"),
	VisibilityOff(identifier="ACTION_58_visibility_off_22"),
	Pause(8),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=192, tiles=2, destinations=["ACTION_58_visibility_on_26"]),
	Jmp(["ACTION_58_visibility_off_22"]),
	VisibilityOn(identifier="ACTION_58_visibility_on_26"),
	SetAllSpeeds(speed=FAST),
	ShiftSouthwestSteps(2),
	Pause(32),
	ShiftNorthwestSteps(2),
	Pause(32),
	Walk1StepNortheast(),
	Pause(16),
	ShiftSoutheastSteps(4),
	Pause(16),
	ShiftSouthwestSteps(2),
	Pause(32),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(3),
	Jmp(["ACTION_58_visibility_off_22"])
])
