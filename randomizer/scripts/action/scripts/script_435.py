#A0435_FLOATING_CHEST

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	JmpToScript(A0014_FLOATING_CHEST)
])
