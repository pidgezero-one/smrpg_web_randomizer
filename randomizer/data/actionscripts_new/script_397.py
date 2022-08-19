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
	FloatingOff(),
	OverwriteSolidity(),
	ShadowOff(),
	SetWalkingSpeed(speed=FASTER),
	SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True),
	VisibilityOn(),
	PlaySound(sound=S048_MINECART_START, channel=4),
	ShiftSouthwestSteps(3),
	OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	FloatingOn(),
	ShadowOn(),
	ShiftSouthwestSteps(18),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthPixels(8),
	SetSpriteSequence(index=1, sprite_offset=3, is_mold=True, is_sequence=True),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	ClearBit(DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING),
	SetBit(TEMP_7043_0),
	Return()
])
