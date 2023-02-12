#A0490_FOREST_DECOY_MUSHROOM

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=3, destinations=["ACTION_490_set_animation_speed_4"], identifier="ACTION_490_db_1"),
	Pause(1),
	Jmp(["ACTION_490_db_1"]),
	SetSequenceSpeed(SLOW, identifier="ACTION_490_set_animation_speed_4"),
	SetSpriteSequence(index=7, looping=False),
	Pause(48),
	SequenceLoopingOn(),
	SetSequenceSpeed(NORMAL),
	Jmp(["ACTION_403_face_mario_9"])
])
