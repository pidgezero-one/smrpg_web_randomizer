# pylint: disable=C0301,C0103

"""referenced by behaviour_53_0x350F7A"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=29,
    script=[
        PlaySound(sound=S0176_BOSS_FADE_OUT_DEATH, identifier="command_0x350ed1"),
        EnableSpritesOnSubscreen(),
        Db(bytearray(b"\x84\x00\x08")),
        Db(bytearray(b"\x9e\x00\x00")),
        PauseScriptUntilBitsClear(768),
        FadeOutSprite(duration=2),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        DisableSpritesOnSubscreen(),
        Db(bytearray(b"\xa4")),
        RemoveObject(),
        SetAMEMToAMEM16Bit(dest_amem=0x6E, amem=0x62),
        Db(bytearray(b"F")),
        Jmp(["command_0x350e93"]),
    ],
)
