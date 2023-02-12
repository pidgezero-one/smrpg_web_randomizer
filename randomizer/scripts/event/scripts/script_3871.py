# E3871_NIMBUS_CASTLE_TWO_CHEST_ROOM_GUARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2384_REFILLED_CHEST_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
