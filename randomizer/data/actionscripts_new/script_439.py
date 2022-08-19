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
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	Pause(2),
	SetWalkingSpeed(speed=SLOW),
	JmpIfVarEqualsConst(TEMP_70AE, 0, ["ACTION_439_visibility_off_57"]),
	BPL262728(),
	Db(bytearray(b'\xc8\x87')),
	SetVarToConst(Z_COORD_2, 12),
	WalkTo70167018701A(),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	JmpIfVarEqualsConst(TEMP_70AE, 25, ["ACTION_439_db_19"]),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x08\x00\x01\x00\x00\x00\x04\x80')),
	SetSpriteSequence(index=6, is_sequence=True, mirror_sprite=True),
	WalkToXYCoords(x=3, y=101, identifier="ACTION_439_walk_to_xy_coords_14"),
	WalkToXYCoords(x=8, y=93),
	WalkToXYCoords(x=14, y=104),
	WalkToXYCoords(x=8, y=93),
	JmpIfVarNotEqualsConst(TEMP_70AE, 25, ["ACTION_439_walk_to_xy_coords_14"]),
	Db(bytearray(b'\xc8\x80'), identifier="ACTION_439_db_19"),
	RunAwayShift(),
	BPL262728(),
	ResetProperties(),
	FixedFCoordOff(),
	FaceMario(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	Inc(PRIMARY_TEMP_700C),
	Mem700CAndConst(0x0007),
	CompareVarToConst(PRIMARY_TEMP_700C, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_439_set_animation_speed_44"]),
	SetSequenceSpeed(speed=SLOW),
	FaceSoutheast(),
	SetSpriteSequence(index=3, looping_off=True, mirror_sprite=True),
	Db(bytearray(b'\xc7\x07')),
	SetBit(TEMP_7044_7),
	Pause(48),
	CreatePacketAt7010WithEvent(packet_id=P028_MUSHROOM_THROWN_SOUTHWEST, event_id=E3077_SHIP_PUZZLE_MUSHROOM, destinations=["ACTION_439_reset_properties_37"]),
	ResetProperties(identifier="ACTION_439_reset_properties_37"),
	SetSequenceSpeed(speed=NORMAL),
	Pause(128),
	SetWalkingSpeed(speed=FAST),
	WalkToXYCoords(x=18, y=73),
	VisibilityOff(),
	Return(),
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_439_set_animation_speed_44"),
	FaceSouthwest(),
	SetSpriteSequence(index=3, looping_off=True),
	Db(bytearray(b'\xc7\x07')),
	Pause(48),
	CreatePacketAt7010WithEvent(packet_id=P028_MUSHROOM_THROWN_SOUTHWEST, event_id=E3077_SHIP_PUZZLE_MUSHROOM, destinations=["ACTION_439_reset_properties_50"]),
	ResetProperties(identifier="ACTION_439_reset_properties_50"),
	SetSequenceSpeed(speed=NORMAL),
	Pause(128),
	SetWalkingSpeed(speed=FAST),
	WalkToXYCoords(x=0, y=73),
	VisibilityOff(),
	Return(),
	VisibilityOff(identifier="ACTION_439_visibility_off_57"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return()
])
