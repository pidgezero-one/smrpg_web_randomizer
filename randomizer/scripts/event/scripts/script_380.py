# E0380_MUSHROOM_KINGDOM_OCCUPIED_VAULT_GUARD_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PauseActionScript(NPC_2),
	SetVarToConst(TEMP_70A9, 22),
	RunEventAsSubroutine(E0278_UNKNOWN),
	SetSyncActionScript(NPC_2, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0656_GUEST_ROOM_ITEM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
