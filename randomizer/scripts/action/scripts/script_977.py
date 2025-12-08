"""A0977_NOTE_WITHOUT_KNIFE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitSet(NOTE_DIRECTION, ["ACTION_977_set_sprite_sequence_3"]),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Jmp(["ACTION_977_set_priority_4"]),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_977_set_sprite_sequence_3"),
        SetPriority(3, identifier="ACTION_977_set_priority_4"),
        ClearBit(NOTE_DIRECTION),
        Return(),
    ]
)
