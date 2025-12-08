# pylint: disable=C0301,C0103

"""referenced by items DUMMY_53SopranoCard"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=69,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x35e9c7"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=4,
            y=-38,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        InitializeBonusMessageSequence(),
        PlaySound(sound=S0006_BONUS_FLOWER_STATUS_UP),
        DisplayBonusMessage(message=BM_ATTACK, x=6, y=0),
        PauseScriptUntilBonusMessageComplete(),
        SetAMEM8BitTo7E1x(0x6F, 0x7EFA1F),
        SetAMEMBits(0x6F, [0]),
        Set7E1xToAMEM8Bit(0x7EFA1F, 0x6F),
        Pause1Frame(),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE014),
        JmpIfAMEM8BitNotEqualsConst(0x6F, 0, ["command_0x35e9f3"]),
        SetAMEM8BitToConst(0x6F, 11),
        DecAMEM8Bit(0x6F, identifier="command_0x35e9f3"),
        JmpIfAMEM8BitNotEqualsConst(0x6F, 1, ["command_0x35e9fe"]),
        RemoveItemFromStandardInventory(LuckyJewel),
        Set7E1xToAMEM8Bit(0x7EE014, 0x6F, identifier="command_0x35e9fe"),
        Pause1Frame(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
    ])
