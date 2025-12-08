# pylint: disable=C0301

"""E0586_GOOMBA_THUMPIN_GOLD_GOOMBA_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_3),
        PlaySound(sound=SO066_KICK_BALL_SHELL, channel=6),
        SetSyncActionScript(MARIO, A0210_GOOMBA_THUMPIN),
        SetSyncActionScript(NPC_7, A0422_GOOMBA_THUMPIN_BONK),
        AddConstToVar(SECONDARY_TEMP_7024, 3),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI0835_DUPLICATE,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False),
        Return(),
    ]
)
