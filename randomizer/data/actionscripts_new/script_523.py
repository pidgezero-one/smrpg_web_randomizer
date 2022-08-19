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
	JmpIfObjectInSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_523_sequence_looping_off_26"], identifier="ACTION_523_jmp_if_object_not_in_level_0"),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=SLOW),
	Pause(120),
	SequenceLoopingOff(),
	JmpIfObjectInSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_523_sequence_looping_off_26"]),
	Pause(120),
	SequenceLoopingOff(),
	Pause(30),
	FaceSouthwest(),
	Pause(30),
	FaceSoutheast(),
	Pause(60),
	JmpIfObjectInSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_523_sequence_looping_off_26"]),
	Pause(60),
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	Pause(120),
	SequenceLoopingOff(),
	JmpIfObjectInSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_523_sequence_looping_off_26"]),
	Pause(30),
	FaceSouthwest(),
	Pause(30),
	FaceSoutheast(),
	Pause(60),
	Jmp(["ACTION_523_jmp_if_object_not_in_level_0"]),
	SequenceLoopingOff(identifier="ACTION_523_sequence_looping_off_26"),
	Pause(60),
	FaceSouthwest(),
	Pause(15),
	FaceSoutheast(),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	FaceSoutheast(),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	SetWalkingSpeed(speed=VERY_FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNortheastSteps(1),
	ShiftNorthwestSteps(12),
	WalkToXYCoords(x=22, y=101),
	FaceNorthwest(),
	FixedFCoordOn(),
	SequencePlaybackOff(),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSouthwestPixels(2, identifier="ACTION_523_shift_southwest_pixels_47"),
	ShiftNortheastPixels(2),
	Jmp(["ACTION_523_shift_southwest_pixels_47"])
])
