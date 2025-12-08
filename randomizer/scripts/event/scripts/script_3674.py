# pylint: disable=C0301

"""E3674_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOWER_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 240, ["EVENT_3674_run_event_as_subroutine_1"]
        ),
        DisableObjectTriggerInSpecificLevel(
            NPC_0,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM),
        DisableObjectTriggerInSpecificLevel(
            NPC_0, R498_NIMBUS_CASTLE_AREA_10_____DUMMY
        ),
        JmpToEvent(
            E0172_CHEST_1_CONTAINER, identifier="EVENT_3674_run_event_as_subroutine_1"
        ),
    ]
)
