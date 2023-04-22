# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack51, monster_attacks Elegy, monster_attacks Backfire, monster_attacks IronMaiden, monster_attacks Fangs, monster_attacks MushFunk, monster_attacks VenomDrool, monster_attacks FunRun, monster_attacks PhysicalAttack46, monster_attacks PollenNap, monster_attacks PhysicalAttack57, monster_attacks PhysicalAttack40, monster_attacks DarkClaw, monster_attacks RoyalFlush, monster_attacks TripleKick, monster_attacks Magnum, monster_attacks PhysicalAttack85, monster_attacks Psyche, monster_attacks PhysicalAttack47, monster_attacks PsychoPlasm, monster_attacks VaVaVoom, monster_attacks PhysicalAttack86, monster_attacks Migraine, monster_attacks Scythe, monster_attacks Sickle, monster_attacks Endobubble, monster_attacks LullaBye"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=75,
    script=[
        ClearAMEM8Bit(0x6F, identifier="command_0x35240c"),
        SetAMEM16BitToConst(0x60, 17),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x35241b"),
        SetAMEM16BitToConst(0x60, 18),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x35242a"),
        SetAMEM16BitToConst(0x60, 19),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x352439"),
        SetAMEM16BitToConst(0x60, 20),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x352448"),
        SetAMEM16BitToConst(0x60, 21),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        AttackTimerBegins(),
        ReturnSubroutine(),
    ],
)
