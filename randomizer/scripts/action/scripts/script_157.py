#A0157_MELODY_BAY_TADPOLES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_157_set_sprite_sequence_3"]),
	PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	SetSpriteSequence(index=10, is_sequence=True, looping=True, identifier="ACTION_157_set_sprite_sequence_3"),
	Pause(12),
	VisibilityOff(),
	Return()
])
