# E3497_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ITEM_GRANTER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3497_pause_0"),
        JmpIfBitClear(TEMP_7043_4, ["EVENT_3497_pause_0"]),
        SetSyncActionScript(NPC_1, A0043_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
        JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_3497_pause_3"]),
        Pause(1, identifier="EVENT_3497_pause"),
        JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_3497_jmp_2"]),
        Jmp(["EVENT_3497_pause"]),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT, identifier="EVENT_3497_jmp_2"),
        Pause(1, identifier="EVENT_3497_pause_3"),
        JmpIfBitClear(TEMP_7043_3, ["EVENT_3497_pause_3"]),
        SetSyncActionScript(NPC_5, A0042_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_RIGHT_GOOMBA),
        Pause(20),
        SetSyncActionScript(NPC_6, A0041_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_LEFT_GOOMBA),
        Return(),
    ]
)
