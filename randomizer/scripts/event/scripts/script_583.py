# E0583_ROSE_TOWN_LIBERATED_TREASURE_HOUSE_BEDROOM_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_583_grant"]),
	DisableObjectTriggerInSpecificLevel(NPC_1, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_583_grant")
])
