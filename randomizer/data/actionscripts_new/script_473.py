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
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(3),
	EndLoop(),
	ShadowOn(),
	Db(bytearray(b' \x05')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x10\x00\x01\x00\x00\x00\x04\x80')),
	ShiftNorthwestSteps(14, identifier="ACTION_473_shift_northwest_steps_9"),
	Walk1StepNortheast(),
	ShiftSoutheastSteps(14),
	Walk1StepSouthwest(),
	Jmp(["ACTION_473_shift_northwest_steps_9"])
])
