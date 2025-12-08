# pylint: disable=C0301

"""E1829_KEEP_DISPLAY_REMAINING_TRIES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        CopyVarToVar(from_var=KEEP_DOOR_LIVES, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_16"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 4),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_14"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 2),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1829_run_dialog_12"]),
        RunDialog(
            dialog_id=DI1319_LAST_CHANCE,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
            bit_6=True),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
        RunDialog(
            dialog_id=DI1318_ONLY_GOT_X_CHANCES_LEFT,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
            bit_6=True,
            identifier="EVENT_1829_run_dialog_12"),
        Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
        RunDialog(
            dialog_id=DI1317_GOT_X_CHANCES,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
            bit_6=True,
            identifier="EVENT_1829_run_dialog_14"),
        Jmp(["EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"]),
        RunDialog(
            dialog_id=DI1316_GOT_X_TRIES,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
            bit_6=True,
            identifier="EVENT_1829_run_dialog_16"),
        ReactivateObject70A8TriggerIfMarioOnTopOfIt(
            identifier="EVENT_1829_reactivate_trigger_if_mario_on_top_of_object_17"
        ),
        Return(),
    ]
)
