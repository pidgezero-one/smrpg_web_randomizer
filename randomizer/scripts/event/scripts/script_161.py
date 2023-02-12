# E0161_NPC_QUEST_GRANT_BEETLEMANIA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(BEETLEMANIA_UNLOCKED),
	RunDialog(dialog_id=DI3074_GOT_BEETLEMANIA, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return()
])
