# E3676_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_FEMALE_NPC

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI3764_NIMBUS_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
