# E3721_NIMBUS_CASTLE_RIGHTMOST_OUTER_CELLAR_GUY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 499, ["EVENT_3721_run_dialog_4"]),
	RunDialog(dialog_id=DI3663_NIMBUS_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3765_NIMBUS_EGG_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3721_run_dialog_4"),
	Return()
])
