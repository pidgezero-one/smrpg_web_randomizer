# pylint: disable=C0301

"""E0588_GOOMBA_THUMPIN_SPINY_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_1),
        PlaySound(sound=SO105_SURPRISE, channel=6),
        SetSyncActionScript(MARIO, A0210_GOOMBA_THUMPIN),
        SetSyncActionScript(NPC_10, A0424_GOOMBA_THUMPIN_SPINY),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_256_ret_0"]),
        Dec(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI0835_DUPLICATE,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        Return(),
    ]
)
