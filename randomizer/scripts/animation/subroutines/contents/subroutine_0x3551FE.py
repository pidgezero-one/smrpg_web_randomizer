# pylint: disable=C0301,C0103

"""referenced by behaviour_46_0x350E98, behaviour_53_0x350F7A, behaviour_37_0x350D36, behaviour_28_0x350BB7, behaviour_44_0x350E4A"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=54,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3551fe"),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x67),
        ClearAMEM8Bit(0x66),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35624B),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35624B),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        ClearAMEM8Bit(0x68),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35624B),
        RunSubroutine(["command_0x352552"]),
        Jmp(["command_0x35252f"]),
    ])
