# pylint: disable=C0301

"""E3879_NIMBUS_CASTLE_BRIDGE_ROOM_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 240, ["EVENT_3879_run_event_as_subroutine_1"]
        ),
        DisableObjectTriggerInSpecificLevel(
            NPC_2,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
        ),
        DisableObjectTriggerInSpecificLevel(
            NPC_0, R500_NIMBUS_CASTLE_AREA_04_____DUMMY
        ),
        JmpToEvent(
            E0172_CHEST_1_CONTAINER, identifier="EVENT_3879_run_event_as_subroutine_1"
        ),
    ]
)
