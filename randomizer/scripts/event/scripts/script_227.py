# E0227_FREESTANDING_15_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_227_room_422_logic"]),
	Return(),
	SetVarToConst(ITEM_ID, FireBomb, identifier="EVENT_227_room_422_logic"),
	JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG)
])
