# pylint: disable=C0301

"""E0160_NPC_QUEST_GRANT_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        JmpIfVarEqualsConst(ITEM_ID, UltraHammer, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Amulet, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AttackScarf, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ExpBooster, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AntidotePin, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AbleJuice, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Energizer, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, IceBomb, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Elixir, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, EarlierTimes, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ElderKey, ["EVENT_160_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_160_run_dialog_104_"]),
        RunDialog(
            dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        AddToInventory(ITEM_ID),
        Return(),
        RunDialog(
            dialog_id=DI0065_GOT_AN_70A7_AWAIT_TERMINATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
            identifier="EVENT_160_run_dialog_104_"),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
