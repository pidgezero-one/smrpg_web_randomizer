# pylint: disable=C0301

"""E0577_ROSE_TOWN_TREASURE_HOUSE_CHEST_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_577_grant"]),
        DisableObjectTriggerInSpecificLevel(
            NPC_1, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F
        ),
        DisableObjectTriggerInSpecificLevel(NPC_1, R094_ROSE_TOWN_TREASURE_HOUSE_1F),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_577_grant"),
    ]
)
