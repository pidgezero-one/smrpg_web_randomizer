# E0428_PIPE_VAULT_THWOMP_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_0),
        JmpIfObjectInSpecificLevel(
            NPC_3, R127_PIPE_VAULT_AREA_02, ["EVENT_428_run_background_event_4"]
        ),
        SummonObjectToSpecificLevel(NPC_3, R127_PIPE_VAULT_AREA_02),
        SummonObjectToCurrentLevel(NPC_3),
        RunBackgroundEvent(
            event_id=E0429_PIPE_VAULT_THWOMP_ROOM_LOADER_BACKGROUND,
            return_on_level_exit=True,
            identifier="EVENT_428_run_background_event_4",
        ),
        RunBackgroundEvent(
            event_id=E0505_PIPE_VAULT_MARIO_THWOMP_TUMBLE,
            return_on_level_exit=True,
            bit_6=True,
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
