# pylint: disable=C0301

"""E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_0, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(NPC_1, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(NPC_2, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(NPC_3, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(NPC_4, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(NPC_5, R477_BOWSERS_KEEP_2ND_TIME_AREA_02),
        SummonObjectToSpecificLevel(
            NPC_1, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM
        ),
        ExitToWorldMap(area=OW04_BOWSERS_KEEP, bit_6=True, bit_7=True),
        Return(),
    ]
)
