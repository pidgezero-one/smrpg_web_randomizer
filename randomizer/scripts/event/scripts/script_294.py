# E0294_MUSHROOM_KINGDOM_INN_NPC

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0605_BERSERK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
