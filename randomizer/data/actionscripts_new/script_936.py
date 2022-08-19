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
	ShadowOff(),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	SetPriority(3),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80')),
	SetWalkingSpeed(speed=VERY_SLOW),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_936_walk_to_xy_coords_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_936_walk_to_xy_coords_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_936_walk_to_xy_coords_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_936_walk_to_xy_coords_26"]),
	WalkToXYCoords(x=5, y=27, identifier="ACTION_936_walk_to_xy_coords_12"),
	ShiftZDownPixels(4),
	ShiftSouthPixels(8),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	Pause(1, identifier="ACTION_936_pause_16"),
	Jmp(["ACTION_936_pause_16"]),
	WalkToXYCoords(x=6, y=26, identifier="ACTION_936_walk_to_xy_coords_18"),
	ShiftZDownPixels(16),
	ShiftEastPixels(3),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	Jmp(["ACTION_936_pause_16"]),
	WalkToXYCoords(x=5, y=25, identifier="ACTION_936_walk_to_xy_coords_23"),
	ShiftZDownPixels(12),
	Jmp(["ACTION_936_pause_16"]),
	WalkToXYCoords(x=5, y=26, identifier="ACTION_936_walk_to_xy_coords_26"),
	ShiftZDownPixels(12),
	Jmp(["ACTION_936_pause_16"])
])
