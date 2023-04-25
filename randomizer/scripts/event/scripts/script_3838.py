# pylint: disable=C0301

"""E3838_KEEP_ANTI_SOFTLOCK_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1221_EXIT_TRAMPOLINE_CONFIRM,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBSelected(["EVENT_3838_ret_2"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
        Return(identifier="EVENT_3838_ret_2"),
    ]
)
