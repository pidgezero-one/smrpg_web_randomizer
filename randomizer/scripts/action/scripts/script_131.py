#A0131_EAST_GUARD_OCCUPIED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_131_set_priority_0"),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(5),
	Pause(1, identifier="ACTION_131_pause_3"),
	JmpIfBitSet(TEMP_7044_4, ["ACTION_131_shift_northwest_steps_6"]),
	Jmp(["ACTION_131_pause_3"]),
	ShiftNorthwestSteps(5, identifier="ACTION_131_shift_northwest_steps_6"),
	Pause(1, identifier="ACTION_131_pause_7"),
	JmpIfBitSet(TEMP_7044_3, ["ACTION_131_set_priority_0"]),
	Jmp(["ACTION_131_pause_7"])
])
