# pylint: disable=C0301

"""E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AE, 3),
        StartLoopNTimes(6),
        JmpIfRandom2of3(
            [
                "EVENT_3511_set_action_script_sync_5",
                "EVENT_3511_set_action_script_sync_7",
            ]
        ),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        Jmp(["EVENT_3511_pause_8"]),
        SetSyncActionScript(
            NPC_1,
            A0709_BOOSTER_HILL_BARREL,
            identifier="EVENT_3511_set_action_script_sync_5",
        ),
        Jmp(["EVENT_3511_pause_8"]),
        SetSyncActionScript(
            NPC_2,
            A0710_BOOSTER_HILL_BARREL,
            identifier="EVENT_3511_set_action_script_sync_7",
        ),
        Pause(210, identifier="EVENT_3511_pause_8"),
        EndLoop(),
        Pause(30),
        StartLoopNTimes(6),
        JmpIfRandom2of3(
            [
                "EVENT_3511_set_action_script_sync_16",
                "EVENT_3511_set_action_script_sync_19",
            ]
        ),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
        Jmp(["EVENT_3511_pause_21"]),
        SetSyncActionScript(
            NPC_1,
            A0709_BOOSTER_HILL_BARREL,
            identifier="EVENT_3511_set_action_script_sync_16",
        ),
        SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
        Jmp(["EVENT_3511_pause_21"]),
        SetSyncActionScript(
            NPC_2,
            A0710_BOOSTER_HILL_BARREL,
            identifier="EVENT_3511_set_action_script_sync_19",
        ),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        Pause(210, identifier="EVENT_3511_pause_21"),
        EndLoop(),
        Pause(30),
        StartLoopNTimes(6),
        SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
        SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
        Pause(210),
        EndLoop(),
        Pause(30),
        Pause(210),
        Pause(210),
        StartLoopNTimes(1),
        Pause(210),
        Pause(210),
        CopyVarToVar(from_var=BOOSTER_HILL_70B1, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 8),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3511_end_loop_41"]),
        PlaySoundBalance(sound=SO014_FLOWER, balance=40),
        SetSyncActionScript(NPC_8, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS),
        EndLoop(identifier="EVENT_3511_end_loop_41"),
        Return(),
    ]
)
