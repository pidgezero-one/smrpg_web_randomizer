# pylint: disable=C0301

"""E3159_PA_MOLE_AFTER_BAMBINO_BOMB"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7043_0),
        JmpIfMarioOnAnObjectOrNot(
            [
                "EVENT_3159_enable_controls_until_return_5",
                "EVENT_3159_enable_controls_until_return_5",
            ]
        ),
        RunDialog(
            dialog_id=DI1638_PA_MOLE_STUCK_AFTER_BOMB,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ClearBit(TEMP_7043_0),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3159_enable_controls_until_return_5",
        ),
        StartLoopNTimes(59),
        Pause(1),
        JmpIfMarioInAir(["EVENT_3159_clear_bit_12"]),
        EndLoop(),
        EnableControlsUntilReturn([]),
        RunDialog(
            dialog_id=DI1646_PA_MOLE_JUMP_ON_HEAD,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ClearBit(TEMP_7043_0, identifier="EVENT_3159_clear_bit_12"),
        Return(),
    ]
)
