# E2352_TOWER_START_BULLET_BILLS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInCurrentLevel(NPC_8, ["EVENT_2352_ret_5"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2352_ret_5"]),
	SetBit(TEMP_7043_1),
	RunBackgroundEvent(event_id=E2351_TOWER_START_BULLET_BILLS_ANIMATION, return_on_level_exit=True),
	SetSyncActionScript(NPC_8, A0386_TOWER_SHOOT_BULLET_BILLS),
	Return(identifier="EVENT_2352_ret_5")
])
