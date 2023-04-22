# pylint: disable=C0301,C0103

"""referenced by items RottenMush, items RockCandy, items AbleJuice, items 79, items MysteryEgg, items Energizer, items Bracer, items Elixir, items BadMushroom, items MaxMushroom, items PureWater, items Mushroom, items RedEssence, items Megalixir, items YoshiAde, items FroggieDrink, items IceBomb, items MukuCookie, items RoyalSyrup, items MidMushroom, items MapleSyrup, items WiltShroom, items HoneySyrup, items SleepyBomb, items FireBomb, items KerokeroCola, items PickMeUp"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=42,
    script=[
        SetAMEMToRandom(amem=0x6E, upper_bound=100, identifier="command_0x35c968"),
        JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 26, ["command_0x35c974"]),
        RunSubroutine(["command_0x35c982"]),
        ReturnSubroutine(identifier="command_0x35c974"),
        SetAMEMToRandom(amem=0x6E, upper_bound=100, identifier="command_0x35c975"),
        JmpIfAMEM8BitGreaterOrEqualThanConst(0x6E, 13, ["command_0x35c981"]),
        RunSubroutine(["command_0x35c982"]),
        ReturnSubroutine(identifier="command_0x35c981"),
        PlaySound(sound=S0006_BONUS_FLOWER_STATUS_UP, identifier="command_0x35c982"),
        DisplayMessage(BATTLE_MESSAGE, 8),
        PauseScriptUntilDialogClosed(),
        SetAMEM16BitTo7E1x(0x60, 0x7EE022),
        IncAMEM16BitByConst(0x60, 96),
        StoreOMEM60ToItemInventory(),
        ReturnSubroutine(),
    ],
)
