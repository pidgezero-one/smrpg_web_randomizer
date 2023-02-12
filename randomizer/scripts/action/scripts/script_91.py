#A0091_BRIDGE_TADPOLE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_91_visibility_on_3"]),
	PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	VisibilityOn(identifier="ACTION_91_visibility_on_3"),
	SetSpriteSequence(index=10, is_sequence=True, looping=True),
	Pause(10),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(5),
	SetWalkingSpeed(FAST),
	ShiftSoutheastPixels(12),
	SetWalkingSpeed(NORMAL),
	ShiftSoutheastPixels(11),
	SetWalkingSpeed(SLOW),
	ShiftSoutheastPixels(9),
	Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
