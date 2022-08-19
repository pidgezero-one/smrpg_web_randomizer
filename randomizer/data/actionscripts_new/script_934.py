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
	SequencePlaybackOff(identifier="ACTION_934_sequence_playback_off_0"),
	SequenceLoopingOff(),
	Pause(2, identifier="ACTION_934_pause_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_934_pause_2"]),
	SequenceLoopingOn(),
	FloatingOff(),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(16),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(8),
	SetWalkingSpeed(speed=SLOW),
	ShiftZUpPixels(4),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZUpPixels(2),
	Pause(12),
	FloatingOn(),
	ClearBit(TEMP_7043_0),
	Jmp(["ACTION_934_sequence_playback_off_0"])
])
