# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=12,
    script=[
        Pause1Frame(identifier="command_0x3a8674"),
        SetAMEM8BitToAMEM(amem=0x68, source_amem=0xC8),
        JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x3a8674"]),
        ReturnSubroutine(),
    ],
)
