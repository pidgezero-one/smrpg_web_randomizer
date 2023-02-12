# E0228_FREESTANDING_14_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_228_room_41_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_228_room_422_logic"]),
	Return(),
	SetVarToConst(ITEM_ID, RoomKey, identifier="EVENT_228_room_41_logic"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
	SetVarToConst(ITEM_ID, RoyalSyrup, identifier="EVENT_228_room_422_logic"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG)
])
