# E1617_MOLEVILLE_OCCUPIED_PA_MOLE_IN_HOUSE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1172_PA_MOLE_INSIDE_MINES_AFTER_BOMB, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
