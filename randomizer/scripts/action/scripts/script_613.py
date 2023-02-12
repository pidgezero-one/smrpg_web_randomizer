#A0613_ROSE_WAY_LAKITU_SHY_GUY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(identifier="ACTION_613_visibility_off_0"),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetPriority(3),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Pause(1),
	JmpIfVarNotEqualsConst(TEMP_70AE, 23, ["ACTION_613_visibility_off_0"]),
	VisibilityOn(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	ShiftSoutheastPixels(18),
	ShiftZDownSteps(3),
	FaceMario(identifier="ACTION_613_face_mario_11"),
	Pause(1),
	Jmp(["ACTION_613_face_mario_11"])
])
