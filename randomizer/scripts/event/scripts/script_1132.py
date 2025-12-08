# pylint: disable=C0301

"""E1132_SEASIDE_OCCUPIED_INNKEEPER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2832_OCCUPIED_SEASIDE_INNKEEPER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBSelected(["EVENT_1132_ret_6"]),
        SetBit(OCCUPIED_SEASIDE_INN),
        Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
        Return(identifier="EVENT_1132_ret_6"),
    ]
)
