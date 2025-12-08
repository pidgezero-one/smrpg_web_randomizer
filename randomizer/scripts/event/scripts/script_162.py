# pylint: disable=C0301

"""E0162_CHEST_GRANT_BEETLEMANIA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        SetVarToConst(Z_COORD_1, 150),
        DecVarFrom7000(Z_COORD_1),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        CreatePacketAt7010(
            packet=P193_BEETLE_CHEST, destinations=["EVENT_162_ret_259"]
        ),
        PlaySound(sound=SO014_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI3077_GOT_BEETLEMANIA,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True),
        SetBit(BEETLEMANIA_UNLOCKED),
        Return(identifier="EVENT_162_ret_259"),
    ]
)
