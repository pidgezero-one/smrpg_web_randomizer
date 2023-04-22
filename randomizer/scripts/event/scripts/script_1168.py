# pylint: disable=C0301

"""E1168_SEASIDE_LIBERATED_INNKEEPER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2916_SEASIDE_INNKEEPER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_1168_run_dialog_17"]),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 15),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1168_set_13"]),
        RunDialog(
            dialog_id=DI2918_SEASIDE_INNKEEPER_INSUFFICIENT_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        StoreCoinCountTo7000(),
        Dec7000FromCoins(),
        SetBit(LIBERATED_SEASIDE_INN),
        Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
        SetVarToConst(PRIMARY_TEMP_7000, 15, identifier="EVENT_1168_set_13"),
        Dec7000FromCoins(),
        SetBit(LIBERATED_SEASIDE_INN),
        Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
        RunDialog(
            dialog_id=DI2917_SEASIDE_INNKEEPER_DECLINE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1168_run_dialog_17",
        ),
        Return(),
    ]
)
