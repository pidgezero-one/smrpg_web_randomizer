#A0614_ROSE_WAY_LAKITU_SHY_GUY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(identifier="ACTION_614_visibility_off_0"),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetPriority(3),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
	Pause(1),
	JmpIfVarNotEqualsConst(TEMP_70AE, 24, ["ACTION_614_visibility_off_0"]),
	VisibilityOn(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	ShiftSoutheastPixels(18),
	ShiftZDownSteps(3),
	FaceMario(identifier="ACTION_614_face_mario_11"),
	Pause(1),
	Jmp(["ACTION_614_face_mario_11"])
])
