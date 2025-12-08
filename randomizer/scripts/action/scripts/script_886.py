"""A0886_NIMBUS_FORKIES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7043_0, identifier="ACTION_886_clear_bit_0"),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 410, ["ACTION_886_clear_bit_34"]),
        SetSpriteSequence(
            index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        JmpIfRandom1of2(["ACTION_886_pause_6"]),
        Pause(8),
        Pause(4, identifier="ACTION_886_pause_6"),
        SetSpriteSequence(
            index=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetSpriteSequence(
            index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(6),
        SetSpriteSequence(
            index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(2),
        SetBit(TEMP_7043_0),
        Pause(2),
        JmpIfRandom1of2(["ACTION_886_set_sprite_sequence_29"]),
        Pause(4),
        SetSpriteSequence(
            index=14,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_886_set_sprite_sequence_29"),
        Pause(30),
        JmpIfRandom1of2(["ACTION_886_clear_bit_0"]),
        Pause(60),
        Jmp(["ACTION_886_clear_bit_0"]),
        ClearBit(TEMP_7043_0, identifier="ACTION_886_clear_bit_34"),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        JmpIfRandom1of2(["ACTION_886_pause_38"]),
        Pause(8),
        Pause(4, identifier="ACTION_886_pause_38"),
        SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
        Pause(6),
        SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
        Pause(2),
        SetBit(TEMP_7043_0),
        Pause(2),
        JmpIfRandom1of2(["ACTION_886_set_sprite_sequence_61"]),
        Pause(4),
        SetSpriteSequence(
            index=14,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_886_set_sprite_sequence_61"),
        Pause(2),
        Pause(10),
        JmpIfRandom1of2(["ACTION_886_clear_bit_34"]),
        Pause(30),
        Jmp(["ACTION_886_clear_bit_34"]),
    ]
)
