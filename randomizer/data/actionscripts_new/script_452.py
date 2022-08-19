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
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, mirror_sprite=True),
	JmpIfBitClear(DIRECTIONAL_7045_7, ["ACTION_452_pause_3"]),
	Pause(176),
	Pause(1, identifier="ACTION_452_pause_3"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=2, destinations=["ACTION_452_sequence_looping_on_6"]),
	Jmp(["ACTION_452_pause_3"]),
	SequenceLoopingOn(identifier="ACTION_452_sequence_looping_on_6"),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True),
	Pause(48),
	ShiftNorthwestSteps(2, identifier="ACTION_452_shift_northwest_steps_9"),
	Pause(8),
	FaceNortheast(),
	Pause(8),
	ShiftSoutheastSteps(2),
	Pause(8),
	FaceSouthwest(),
	Pause(8),
	Jmp(["ACTION_452_shift_northwest_steps_9"])
])
