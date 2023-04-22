# pylint: disable=C0301

"""E0606_MARRYMORE_INN_LOBBY_GUEST_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2056_HOTEL_TIP_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
