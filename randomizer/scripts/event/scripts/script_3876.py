# E3876_NIMBUS_CASTLLE_4_WAY_PATH_LEFT_GUARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2389_TALK_TO_NPCS_AGAIN_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
