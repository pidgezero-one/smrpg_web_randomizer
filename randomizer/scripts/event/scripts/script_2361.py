# E2361_ABYSS_AMEBOID_BUTTON_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_10, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_11, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_12, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_13, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_14, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        SummonObjectToSpecificLevel(NPC_15, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
        JmpIfBitClear(ABYSS_GREEN_BUTTON, ["EVENT_2361_set_action_script_sync_8"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        SetSyncActionScript(
            NPC_1,
            A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT,
            identifier="EVENT_2361_set_action_script_sync_8",
        ),
        SetSyncActionScript(NPC_2, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
        SetSyncActionScript(NPC_3, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
        SetSyncActionScript(NPC_4, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
        SetAsyncActionScript(NPC_5, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
        SetSyncActionScript(NPC_1, A0457_FACTORY_SWITCH_ROOM_AMEBOID),
        SetSyncActionScript(NPC_2, A0459_FACTORY_SWITCH_ROOM_AMEBOID),
        SetSyncActionScript(NPC_3, A0461_FACTORY_SWITCH_ROOM_AMEBOID),
        SetSyncActionScript(NPC_4, A0463_FACTORY_SWITCH_ROOM_AMEBOID),
        SetSyncActionScript(NPC_5, A0481_FACTORY_SWITCH_ROOM_AMEBOID),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
