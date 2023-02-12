# E0242_CHEST_6_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_242_room_144_446_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_242_room_144_446_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_242_room_455_logic"]),
	Return(),
	SetVarToConst(ITEM_ID, RockCandy, identifier="EVENT_242_room_144_446_logic"),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
	JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_242_room_455_logic")
])
