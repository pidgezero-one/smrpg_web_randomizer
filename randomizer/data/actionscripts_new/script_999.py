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
	FaceNorthwest(),
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	Pause(1, identifier="ACTION_999_pause_3"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_999_clear_solidity_bits_6"]),
	Jmp(["ACTION_999_pause_3"]),
	ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_999_clear_solidity_bits_6"),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=FAST),
	JumpToHeight(height=96, silent=True),
	ShiftNorthwestSteps(2),
	SequenceLoopingOff(),
	Pause(30),
	Jmp(["ACTION_997_sequence_playback_on_0"])
])
