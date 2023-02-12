# E1430_MUSHROOM_WAY_2_SPINNING_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInSpecificLevel(NPC_4, R204_MUSHROOM_WAY_AREA_02, ["EVENT_1430_ret_4"]),
	SetVarToConst(X_COORD_2, 2331),
	MoveScriptToMainThread(),
	RunEventAsSubroutine(E1537_SPINNING_FLOWER_CORE_LOGIC),
	Return(identifier="EVENT_1430_ret_4")
])
