# E0695_MARRYMORE_GREEN_KID

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_695_run_dialog_8"]),
	RunDialog(dialog_id=DI2120_SHAKING_TOAD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2172_CHAPEL_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_695_run_dialog_8"),
	Return()
])
