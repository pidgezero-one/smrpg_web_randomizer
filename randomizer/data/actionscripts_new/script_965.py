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
	ShadowOff(identifier="ACTION_965_shadow_off_0"),
	SetWalkingSpeed(speed=SLOW),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	WalkToXYCoords(x=7, y=94),
	ShiftSoutheastPixels(9),
	SetBit(TEMP_7043_0),
	WalkToXYCoords(x=9, y=99),
	ShiftSoutheastPixels(9),
	SetBit(TEMP_7043_1),
	WalkToXYCoords(x=12, y=105),
	ShiftSoutheastPixels(9),
	SetBit(TEMP_7043_2),
	Walk1StepSoutheast(),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	WalkToXYCoords(x=16, y=113),
	ShiftToXYCoords(x=14, y=52),
	ShiftSoutheastSteps(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	ShiftToXYCoords(x=6, y=92),
	Jmp(["ACTION_965_shadow_off_0"])
])
