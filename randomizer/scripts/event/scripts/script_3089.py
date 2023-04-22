# pylint: disable=C0301

"""E3089_GRANT_ITEM_FROM_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO014_FLOWER, channel=6),
        JmpIfVarEqualsConst(ITEM_ID, UltraHammer, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, Amulet, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, AttackScarf, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, ExpBooster, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, AntidotePin, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, AbleJuice, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, Energizer, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, IceBomb, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, Elixir, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, EarlierTimes, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, ElderKey, ["EVENT_3089_run_dialog_25_"]),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_3089_run_dialog_25_"]),
        RunDialog(
            dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True,
        ),
        AddToInventory(ITEM_ID),
        Return(),
        RunDialog(
            dialog_id=DI1178_FOUND_AN_70A7_AUTO_TERMINATE,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True,
            identifier="EVENT_3089_run_dialog_25_",
        ),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
