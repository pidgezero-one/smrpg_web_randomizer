"""A0860_ABYSS_BEFORE_1ST_BOSS_JUMP_BACK_UP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNortheast(),
        SetSpriteSequence(
            index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True
        ),
        SetPriority(3),
        Db(bytearray(b" \x07")),
        Db(bytearray(b"$ \x01\xc0\xfe")),
        Db(bytearray(b"%\x00\x0e\x80\xff")),
        Pause(46),
        BPL262728(),
        PlaySound(sound=SO058_INSERT, channel=4),
        OverwriteSolidity(
            cant_pass_walls=True,
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
        ),
        Return(),
    ]
)
