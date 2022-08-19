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
	Pause(32),
	JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	Walk1StepSouthwest(),
	FaceNorthwest(),
	Pause(160),
	Walk1StepNortheast(),
	JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	Return()
])
