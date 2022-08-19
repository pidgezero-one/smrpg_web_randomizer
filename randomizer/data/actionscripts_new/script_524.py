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
	SequenceLoopingOff(identifier="ACTION_524_sequence_looping_off_0"),
	JmpIfObjectInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	Pause(120),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=NORMAL),
	JmpIfObjectInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	Pause(120),
	SequenceLoopingOff(),
	JmpIfObjectInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	Pause(120),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=SLOW),
	Pause(60),
	SequenceLoopingOff(),
	Pause(60),
	JmpIfObjectInSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["ACTION_524_sequence_looping_off_28"]),
	JumpToHeight(64),
	Pause(15),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=FAST),
	Pause(45),
	SequenceLoopingOff(),
	Pause(30),
	FaceSouthwest(),
	Pause(30),
	FaceNorthwest(),
	Pause(60),
	Jmp(["ACTION_524_sequence_looping_off_0"]),
	SequenceLoopingOff(identifier="ACTION_524_sequence_looping_off_28"),
	Pause(60),
	FaceSouthwest(),
	Pause(15),
	FaceNorthwest(),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	FaceNorthwest(),
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
	ShiftSouthwestPixels(2, identifier="ACTION_524_shift_southwest_pixels_49"),
	ShiftNortheastPixels(2),
	Jmp(["ACTION_524_shift_southwest_pixels_49"])
])
