# E0576_ROSE_TOWN_TREASURE_HOUSE_CHEST_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_576_grant"]),
	DisableObjectTriggerInSpecificLevel(NPC_0, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	DisableObjectTriggerInSpecificLevel(NPC_0, R094_ROSE_TOWN_TREASURE_HOUSE_1F),
	JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_576_grant")
])
