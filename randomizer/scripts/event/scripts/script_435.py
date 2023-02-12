# E0435_PIPE_VAULT_ROOM_1_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_435_action_queue_sync_3"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=10, y=10, z=2, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        Jmp(["EVENT_435_jmp_if_object_not_in_level_4"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=4, y=22, z=2, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_435_action_queue_sync_3",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R123_PIPE_VAULT_AREA_01,
            ["EVENT_435_jmp_if_object_not_in_level_6"],
            identifier="EVENT_435_jmp_if_object_not_in_level_4",
        ),
        ActionQueueSync(target=NPC_1, subscript=[ASVisibilityOff()]),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R123_PIPE_VAULT_AREA_01,
            ["EVENT_435_jmp_if_object_not_in_level_8"],
            identifier="EVENT_435_jmp_if_object_not_in_level_6",
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASVisibilityOff()]),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R123_PIPE_VAULT_AREA_01,
            ["EVENT_435_jmp_if_object_not_in_level_10"],
            identifier="EVENT_435_jmp_if_object_not_in_level_8",
        ),
        ActionQueueSync(target=NPC_3, subscript=[ASVisibilityOff()]),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R123_PIPE_VAULT_AREA_01,
            ["EVENT_435_run_background_event_12"],
            identifier="EVENT_435_jmp_if_object_not_in_level_10",
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASVisibilityOff()]),
        RunBackgroundEvent(
            event_id=E3329_JUMPING_FIREBALLS,
            return_on_level_exit=True,
            identifier="EVENT_435_run_background_event_12",
        ),
        JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_256_ret_0"]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
