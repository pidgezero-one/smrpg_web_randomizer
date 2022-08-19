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
	ShadowOn(),
	StartLoopNTimes(2),
	Pause(1, identifier="ACTION_39_pause_2"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_39_pause_2"]),
	TransferToXYZF(x=29, y=29, z=0, direction=EAST),
	SetPriority(3),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	VisibilityOn(),
	SetWalkingSpeed(speed=FAST),
	JumpToHeight(96),
	ShiftSoutheastSteps(3),
	VisibilityOff(),
	ClearBit(TEMP_7043_1),
	EndLoop(),
	Pause(1, identifier="ACTION_39_pause_15"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_39_pause_15"]),
	SetSpriteSequence(index=0, is_sequence=True),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	VisibilityOn(),
	Db(bytearray(b'\x97\x17'), identifier="ACTION_39_db_20"),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_39_db_20"]),
	JumpToHeight(120),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNorthwest(),
	ShiftNorthwestPixels(4),
	FloatingOff(),
	Return()
])
