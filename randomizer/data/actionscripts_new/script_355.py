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
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=16, y=24),
	Jmp(["ACTION_355_set_animation_speed_10"]),
	ShadowOff(identifier="ACTION_355_shadow_off_3"),
	FaceSouth(),
	FixedFCoordOn(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	SetWalkingSpeed(speed=FAST),
	Return(),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_355_set_animation_speed_10"),
	SetSolidityBits(cant_pass_walls=True),
	PlaySound(sound=S028_PIPE_ENTRANCE, channel=6),
	SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True),
	ClearSolidityBits(cant_pass_walls=True),
	DecZCoord1Step(),
	SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	ResetProperties(),
	FixedFCoordOff(),
	Return()
])
