# E0743_NIMBUS_LAND_LIBERATED_CASTLE_MAIN_HALLWAY_MAN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0037_NIMBUS_NPC_LINK_SAMUS_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
