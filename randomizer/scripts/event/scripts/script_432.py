# pylint: disable=C0301

"""E0432_PIPE_VAULT_GOOMBA_THUMPIN_EXIT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CloseDialog(),
        StopAllBackgroundEvents(),
        StopBackgroundEvent(TIMER_701C),
        ClearBit(TEMP_7049_6),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES,
            face_direction=NORTHEAST,
            x=13,
            y=38,
            z=1,
            run_entrance_event=True),
        SetBit(TEMP_7044_6),
        Return(),
    ]
)
