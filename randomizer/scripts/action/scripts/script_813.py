"""A0813_NIMBUS_NPC_RANDOM_DIRECTIONS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80")
        ),
        SetSolidityBits(cant_pass_npcs=True),
        SetSolidityBits(cant_pass_walls=True),
        Jmp(["ACTION_128_set_object_memory_bits_0"]),
    ]
)
