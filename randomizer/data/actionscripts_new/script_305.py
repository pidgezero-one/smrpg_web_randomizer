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
	ShiftSoutheastPixels(8),
	SetSequenceSpeed(speed=VERY_SLOW),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0006),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_305_pause_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_305_pause_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_305_pause_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_305_jmp_to_subroutine_12"]),
	Pause(80, identifier="ACTION_305_pause_9"),
	Pause(80, identifier="ACTION_305_pause_10"),
	Pause(80, identifier="ACTION_305_pause_11"),
	JmpToSubroutine(["ACTION_304_visibility_on_21"], identifier="ACTION_305_jmp_to_subroutine_12"),
	TransferXYZFSteps(x=2, y=4, z=20, direction=NORTHEAST),
	Pause(40),
	JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	TransferXYZFSteps(x=253, y=254, z=20, direction=NORTHEAST),
	Pause(40),
	JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	TransferXYZFSteps(x=1, y=254, z=20, direction=NORTHEAST),
	Pause(40),
	Jmp(["ACTION_305_jmp_to_subroutine_12"])
])
