# E3747_NIMBUS_HOT_SPRING_GUARDS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(HOT_SPRING_GUARD_POSITION, ["EVENT_3747_run_dialog_199"]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3747_run_dialog_199"]),
	RunDialog(dialog_id=DI3721_HOT_SPRING_GUARD_OCCUPIED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3710_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3747_run_dialog_199"),
	Return()
])
