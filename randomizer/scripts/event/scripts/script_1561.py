# E1561_LANDS_END_GECKIT_CANNON_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_0, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SummonObjectToSpecificLevel(NPC_1, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SummonObjectToSpecificLevel(NPC_2, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SummonObjectToSpecificLevel(NPC_3, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SummonObjectToSpecificLevel(NPC_4, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SummonObjectToSpecificLevel(NPC_5, R141_LANDS_END_AREA_04_ROTATING_FLOWERS),
        SetBit(TEMP_7044_2),
        ActionQueueSync(
            target=NPC_0, subscript=[ASShiftWestPixels(4), ASFaceSoutheast()]
        ),
        FadeInFromBlack(sync=False),
        RunBackgroundEvent(
            event_id=E1612_SUMMON_GECKITS_IN_CANNON_ROOM, return_on_level_exit=True
        ),
        Return(),
    ]
)
