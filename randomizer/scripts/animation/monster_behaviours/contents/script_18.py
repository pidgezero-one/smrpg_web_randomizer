# behaviour_18_0x35099D

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=56,
    script=[
        Db(bytearray(b"X")),
        Db(bytearray(b"Y")),
        JmpIfTargetDisabled(["command_0x350a38"]),
        VisibilityOn(),
        SetAMEM8BitTo7E5x(0x60, 0x7E002E),
        ClearAMEM8Bit(0x61),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352128),
        Db(bytearray(b"\x16")),
        MoveObject(
            speed=11,
            start_position=-161,
            end_position=160,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
            identifier="command_0x3509ae",
        ),
        Db(bytearray(b"\x12\x81")),
        SetAMEM40ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_x=True),
        PauseScriptUntil(condition=0x01),
        ResetTargetMappingMemory(),
        Db(bytearray(b"\x15")),
        MoveObject(
            speed=11,
            start_position=160,
            end_position=-161,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            set_speed=True,
        ),
        Db(bytearray(b"\x12A")),
        Db(bytearray(b"\x15")),
        Pause1Frame(),
        Jmp(["command_0x3509ae"]),
    ],
)
