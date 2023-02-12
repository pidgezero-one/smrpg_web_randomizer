# E0229_FREESTANDING_13_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_229_room_41_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_229_room_422_logic"]),
	Return(),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_229_room_41_logic"),
	SetVarToConst(ITEM_ID, MaxMushroom, identifier="EVENT_229_room_422_logic"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG)
])
