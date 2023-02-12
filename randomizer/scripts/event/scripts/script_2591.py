# E2591_SNIFIT_8

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2591_run_dialog_4"]),
	RunDialog(dialog_id=DI3096_APPRENTICE_REJECTED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_0),
	Return(),
	RunDialog(dialog_id=DI3097_APPRENTICE_REJECTED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2591_run_dialog_4"),
	Return()
])
