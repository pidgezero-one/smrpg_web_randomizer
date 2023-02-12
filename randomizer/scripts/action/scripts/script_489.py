#A0489_FOREST_MAZE_AREA_DECOY_MUSHROOM

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=3, destinations=["ACTION_489_set_animation_speed_4"], identifier="ACTION_489_db_1"),
	Pause(1),
	Jmp(["ACTION_489_db_1"]),
	SetSequenceSpeed(SLOW, identifier="ACTION_489_set_animation_speed_4"),
	SetSpriteSequence(index=7, looping=False),
	Pause(48),
	SequenceLoopingOn(),
	SetSequenceSpeed(NORMAL),
	Jmp(["ACTION_405_sequence_looping_on_0"])
])
