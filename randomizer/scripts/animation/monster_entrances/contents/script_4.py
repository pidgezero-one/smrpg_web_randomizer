# ENT0004_DROP_FROM_ABOVE

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=-176,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        SetAMEM8BitTo7E5x(0x60, 0x7E001D),
        JmpIfAMEMBitsSet(0x60, [1], ["command_0x3521ef"]),
        Db(bytearray(b"\x18\x00\x80")),
        ResetSpriteSequence(),
        MoveObject(
            speed=161,
            start_position=0,
            end_position=4096,
            apply_to_z=True,
            set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
            identifier="command_0x3521ef",
        ),
        Pause1Frame(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        PauseScriptUntil(condition=0x01),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
