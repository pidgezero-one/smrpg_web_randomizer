# E1642_BOOSTER_PASS_SECRET_HINT_GUY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["EVENT_1642_run_dialog_3"]),
	RunDialog(dialog_id=DI1140_TOWER_DESCRIPTION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1250_BOOSTER_PASS_SECRET_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1642_run_dialog_3"),
	Return()
])
