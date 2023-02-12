# E3186_MOLES_IN_FIRST_MINES_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1631_MOUNTAIN_ENTRANCE_GUYS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
