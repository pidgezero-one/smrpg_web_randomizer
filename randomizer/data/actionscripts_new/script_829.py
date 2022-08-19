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
	SetSpriteSequence(index=0, is_sequence=True),
	SetPriority(3),
	SetWalkingSpeed(speed=NORMAL),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 28, ["ACTION_829_shift_f_direction_steps_9"]),
	ShiftFDirectionSteps(8, identifier="ACTION_829_shift_f_direction_steps_5"),
	Pause(16),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_829_shift_f_direction_steps_5"]),
	ShiftFDirectionSteps(2, identifier="ACTION_829_shift_f_direction_steps_9"),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	Jmp(["ACTION_829_shift_f_direction_steps_9"])
])
