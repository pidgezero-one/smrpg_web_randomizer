# pylint: disable=C0301

"""E1873_MIDAS_RIVER_SIGN_AFTER_BUCKET_WARP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1315_MIDAS_RIVER_CLOSED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1873_ret_7"]),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        AddCoins(PRIMARY_TEMP_7000),
        PlaySound(sound=SO013_COIN, channel=6),
        RunDialog(
            dialog_id=DI1311_RECEIVED_X_COINS,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        SetBit(TEMP_7044_6),
        Return(identifier="EVENT_1873_ret_7"),
    ]
)
