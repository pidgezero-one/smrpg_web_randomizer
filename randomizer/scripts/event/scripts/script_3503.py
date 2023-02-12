# E3503_BOOSTER_HILL_BARREL_SUMMONER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AE, 3),
        StartLoopNTimes(6),
        SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
        Pause(210),
        EndLoop(),
        JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_3503_pause_9"]),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_3503_pause_9"]),
        SetBit(TEMP_7043_7),
        SetSyncActionScript(NPC_7, A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD),
        Pause(30, identifier="EVENT_3503_pause_9"),
        SetVarToConst(TEMP_70AE, 2),
        StartLoopNTimes(6),
        JmpIfRandom2of3(
            [
                "EVENT_3503_set_action_script_sync_16",
                "EVENT_3503_set_action_script_sync_19",
            ]
        ),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
        Jmp(["EVENT_3503_pause_21"]),
        SetSyncActionScript(
            NPC_1,
            A0709_BOOSTER_HILL_BARREL,
            identifier="EVENT_3503_set_action_script_sync_16",
        ),
        SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
        Jmp(["EVENT_3503_pause_21"]),
        SetSyncActionScript(
            NPC_2,
            A0710_BOOSTER_HILL_BARREL,
            identifier="EVENT_3503_set_action_script_sync_19",
        ),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        Pause(210, identifier="EVENT_3503_pause_21"),
        EndLoop(),
        Pause(30),
        SetVarToConst(TEMP_70AE, 1),
        StartLoopNTimes(6),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
        Pause(210),
        EndLoop(),
        Pause(30),
        SetVarToConst(TEMP_70AE, 0),
        SetBit(TEMP_7043_3),
        SetTempAsyncActionScript(NPC_4, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
        SetTempAsyncActionScript(NPC_5, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
        ActionQueueAsync(target=NPC_3, subscript=[ASWalk1StepNortheast()]),
        SetTempAsyncActionScript(NPC_3, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
        Return(),
    ]
)
