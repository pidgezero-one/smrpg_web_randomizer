# pylint: disable=C0301,C0103

"""referenced by monster_attacks SporeChimes, monster_attacks FearRoulette, monster_attacks Grinder, monster_attacks Chomp, monster_attacks PhysicalAttack21, monster_attacks PhysicalAttack50, monster_attacks LocoExpress, monster_attacks PhysicalAttack90, monster_attacks PhysicalAttack29, behaviour_22_0x350A3E, monster_attacks BombsAway, monster_attacks PhysicalAttack18, monster_attacks GunkBall, monster_attacks 117, monster_attacks 114, monster_attacks PhysicalAttack5, monster_attacks WildCard, monster_attacks 122, monster_attacks PhysicalAttack27, monster_attacks PhysicalAttack10, monster_attacks PhysicalAttack115, monster_attacks PhysicalAttack4, monster_attacks ScrowDust, monster_attacks 118, monster_attacks Claw, monster_attacks ScrowBell, monster_attacks Missedme, monster_attacks PhysicalAttack7, monster_attacks PhysicalAttack101, monster_attacks PhysicalAttack93, monster_attacks PhysicalAttack95, monster_attacks PhysicalAttack108, behaviour_40_0x350DA3, monster_attacks PhysicalAttack9, monster_attacks PhysicalAttack15, monster_attacks PhysicalAttack20, monster_attacks DoomReverb, monster_attacks PhysicalAttack11, monster_attacks FlutterHush, monster_attacks PhysicalAttack28, monster_attacks PhysicalAttack105, monster_attacks 126, monster_attacks Funguspike, monster_attacks FullHouse, monster_attacks Multistrike, monster_attacks Terrapunch, monster_attacks PhysicalAttack56, behaviour_31_0x350BFD, monster_attacks Stench, monster_attacks PhysicalAttack31, monster_attacks PhysicalAttack94, monster_attacks Thornet, monster_attacks PhysicalAttack91, monster_attacks Blazer, behaviour_15_0x35091C, monster_attacks PhysicalAttack2, monster_attacks PhysicalAttack81, monster_attacks DahliaDance, monster_attacks InkBlast, monster_attacks LastShot, monster_attacks Echofinder, monster_attacks ViroPlasm, monster_attacks Skewer, monster_attacks CarniKiss, monster_attacks Poison, monster_attacks PhysicalAttack12, monster_attacks 124, monster_attacks Pierce, monster_attacks BodySlam, monster_attacks Deathsickle, monster_attacks 115, behaviour_7_0x350796, monster_attacks SpritzBomb, monster_attacks GetTough, monster_attacks PhysicalAttack107, monster_attacks PhysicalAttack0, monster_attacks 127, monster_attacks PhysicalAttack89, behaviour_50_0x350F4A, monster_attacks 116"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=57,
    script=[
        AttackTimerBegins(identifier="command_0x3523c4"),
        ClearAMEM8Bit(0x6F),
        Db(bytearray(b"?\x80\x15\x00\x00\x84")),
        PauseScriptUntilAMEMBitsSet(0x6F, [0, 1, 2, 3, 4, 5, 6, 7]),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x3523d1"),
        SetAMEM16BitToConst(0x60, 13),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x3523df"),
        SetAMEM16BitToConst(0x60, 14),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x3523ee"),
        SetAMEM16BitToConst(0x60, 15),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
    ],
)
