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
	SetVarToConst(SECONDARY_TEMP_7024, 20),
	SetWalkingSpeed(speed=NORMAL),
	Set700CToPressedButton(),
	DecVarFrom700C(SECONDARY_TEMP_7024),
	Mem700CAndConst(0x0003),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_36_load_mem_11"]),
	Db(bytearray(b'\xc8\x07')),
	AddConstToVar(Z_COORD_2, 128),
	AddConstToVar(X_COORD_2, 64),
	TransferTo70167018701A(),
	Jmp(["ACTION_36_visibility_on_16"]),
	LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_36_load_mem_11"),
	Pause(8),
	EndLoop(),
	Pause(1),
	SetSequenceSpeed(speed=FAST),
	VisibilityOn(identifier="ACTION_36_visibility_on_16"),
	SetPriority(3),
	ShiftNorthwestSteps(4),
	Jmp(["ACTION_32_shift_z_up_steps_20"]),
	Return()
])
