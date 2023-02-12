# E3650_NIMBUS_OCCUPIED_NORTHEAST_HOUSE_RIGHT_WOMAN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI3591_NIMBUS_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
