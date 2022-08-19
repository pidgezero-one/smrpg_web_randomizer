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
	SetWalkingSpeed(speed=SLOW),
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	ShiftNorthwestPixels(37, identifier="ACTION_548_shift_northwest_pixels_7"),
	JmpIfRandom1of2(["ACTION_548_shift_northwest_pixels_30"]),
	SetSpriteSequence(index=9, is_sequence=True),
	JmpIfVarEqualsConst(GAME_OVER_COUNTER_MAYBE, 0, ["ACTION_548_pause_16"]),
	StartLoopNTimes(4),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=128, tiles=3, destinations=["ACTION_549_dec_0"]),
	Pause(16),
	EndLoop(),
	Jmp(["ACTION_548_reset_properties_17"]),
	Pause(80, identifier="ACTION_548_pause_16"),
	ResetProperties(identifier="ACTION_548_reset_properties_17"),
	JmpIfRandom1of2(["ACTION_548_shift_northwest_pixels_30"]),
	FaceNortheast(),
	Pause(8),
	FaceSoutheast(),
	Pause(8),
	ShiftSoutheastPixels(37),
	Pause(8),
	FaceSouthwest(),
	Pause(8),
	FaceNorthwest(),
	Pause(16),
	Jmp(["ACTION_548_shift_northwest_pixels_7"]),
	ShiftNorthwestPixels(37, identifier="ACTION_548_shift_northwest_pixels_30"),
	Pause(8),
	FaceNortheast(),
	Pause(8),
	FaceSoutheast(),
	Pause(16),
	Jmp(["ACTION_547_shift_southeast_pixels_7"])
])
