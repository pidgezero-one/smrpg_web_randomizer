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
	JmpIfBitSet(UNKNOWN_7078_1, ["ACTION_162_set_animation_speed_57"]),
	JmpIfBitSet(UNKNOWN_7078_0, ["ACTION_162_set_animation_speed_38"]),
	JmpIfBitSet(UNKNOWN_7077_7, ["ACTION_162_set_animation_speed_18"]),
	VisibilityOn(),
	SetBit(UNKNOWN_7077_7),
	SequenceLoopingOn(),
	SetAllSpeeds(speed=FASTER),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	JumpToHeight(128),
	WalkToXYCoords(x=20, y=108),
	ShiftNorthSteps(7),
	StartLoopNTimes(1),
	ShiftNortheastSteps(3),
	SetAllSpeeds(speed=FAST),
	ShiftNortheastSteps(2),
	SetAllSpeeds(speed=FASTER),
	EndLoop(),
	ShiftNorthwestSteps(2),
	SetAllSpeeds(speed=FASTER, identifier="ACTION_162_set_animation_speed_18"),
	TransferToXYZF(x=24, y=82, z=0, direction=EAST),
	VisibilityOn(),
	FaceSouthwest(),
	Pause(1, identifier="ACTION_162_pause_22"),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_162_set_bit_25"]),
	Jmp(["ACTION_162_pause_22"]),
	SetBit(UNKNOWN_7078_0, identifier="ACTION_162_set_bit_25"),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	JumpToHeight(128),
	SetPriority(3),
	WalkToXYCoords(x=29, y=72),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	SetAllSpeeds(speed=VERY_FAST),
	ShiftNorthwestSteps(9),
	SetAllSpeeds(speed=FASTER),
	ShiftNorthSteps(5),
	ShiftNorthwestSteps(2),
	ShiftNorthSteps(3),
	ShiftNortheastSteps(2),
	SetAllSpeeds(speed=FAST, identifier="ACTION_162_set_animation_speed_38"),
	TransferToXYZF(x=24, y=43, z=0, direction=EAST),
	VisibilityOn(),
	FaceSouthwest(),
	Pause(1, identifier="ACTION_162_pause_42"),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=3, destinations=["ACTION_162_set_bit_45"]),
	Jmp(["ACTION_162_pause_42"]),
	SetBit(UNKNOWN_7078_1, identifier="ACTION_162_set_bit_45"),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	JumpToHeight(128),
	WalkToXYCoords(x=25, y=36),
	SetAllSpeeds(speed=FASTER),
	ShiftNorthwestSteps(4),
	SetAllSpeeds(speed=FAST),
	ShiftNorthwestSteps(4),
	SetAllSpeeds(speed=FASTER),
	ShiftNorthSteps(5),
	SetAllSpeeds(speed=FAST),
	ShiftNorthwestSteps(2),
	SetAllSpeeds(speed=FAST, identifier="ACTION_162_set_animation_speed_57"),
	TransferToXYZF(x=20, y=16, z=0, direction=EAST),
	VisibilityOn(),
	FaceSoutheast(),
	Pause(1, identifier="ACTION_162_pause_61"),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_162_set_bit_64"]),
	Jmp(["ACTION_162_pause_61"]),
	SetBit(BANDITS_WAY_CUTSCENE_3_VIEWED, identifier="ACTION_162_set_bit_64"),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	JumpToHeight(144),
	ShiftNortheastSteps(5),
	VisibilityOff(),
	Return()
])
