# pylint: disable=C0301

"""E3286_SHIP_INTERACT_WITH_BOSS_AFTER_WINNING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioOnAnObjectOrNot(
            [
                "EVENT_3286_enable_controls_until_return_6",
                "EVENT_3286_enable_controls_until_return_6",
            ]
        ),
        JmpIfBitClear(JOHNNY_POSITION, ["EVENT_3286_run_dialog_4"]),
        RunDialog(
            dialog_id=DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        RunDialog(
            dialog_id=DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3286_run_dialog_4"),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3286_enable_controls_until_return_6"),
        StartLoopNTimes(59),
        Pause(1),
        JmpIfMarioInAir(["EVENT_3286_ret_13"]),
        EndLoop(),
        EnableControlsUntilReturn([]),
        RunDialog(
            dialog_id=DI1781_SHIP_BOSS_JUMP_ON_HEAD,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(identifier="EVENT_3286_ret_13"),
    ]
)
