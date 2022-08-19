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
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_307_jmp_to_subroutine_6"]),
	Pause(80),
	JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_307_jmp_to_subroutine_6"),
	TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	Pause(40),
	Jmp(["ACTION_307_jmp_to_subroutine_6"])
])
