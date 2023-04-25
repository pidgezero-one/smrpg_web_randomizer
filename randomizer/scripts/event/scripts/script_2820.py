# pylint: disable=C0301

"""E2820_ASYNC_NO_ANIMATION_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        JmpIfVarEqualsConst(ITEM_ID, UltraHammer, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Amulet, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AttackScarf, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ExpBooster, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AntidotePin, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AbleJuice, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Energizer, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, IceBomb, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Elixir, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, EarlierTimes, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ElderKey, ["EVENT_2820_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_2820_run_dialog_104_"]),
        RunDialog(
            dialog_id=DI0066_GOT_A_70A7_AUTO_TERMINATE,
            above_object=BOWSER,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        Return(),
        RunDialog(
            dialog_id=DI0064_GOT_AN_70A7_AUTO_TERMINATE,
            above_object=BOWSER,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            identifier="EVENT_2820_run_dialog_104_",
        ),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
