#A0799_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(NORMAL, identifier="ACTION_799_set_animation_speed_0"),
	SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(66),
	ResetProperties(),
	FaceNorthwest(),
	SetSequenceSpeed(VERY_FAST),
	Return()
])
