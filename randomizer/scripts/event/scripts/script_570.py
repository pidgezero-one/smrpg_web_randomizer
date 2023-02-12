# E0570_ROSE_TOWN_LIBERATED_RIGHT_BLUE_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_570_run_dialog_0"]),
	RunDialog(dialog_id=DI0874_GARDENER_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0861_GARDENER_HIDDEN_ITEM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_570_run_dialog_0"),
	Return()
])
