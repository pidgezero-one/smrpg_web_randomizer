# pylint: disable=C0301

"""E0165_FREESTANDING_GRANT_ITEM_BAG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ]),
        JmpIfVarEqualsConst(ITEM_ID, UltraHammer, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Amulet, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AttackScarf, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ExpBooster, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AntidotePin, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AbleJuice, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Energizer, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, IceBomb, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, Elixir, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, EarlierTimes, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, ElderKey, ["EVENT_165_run_dialog_104_"]),
        JmpIfVarEqualsConst(ITEM_ID, AltoCard, ["EVENT_165_run_dialog_104_"]),
        RunDialog(
            dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True),
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
            identifier="EVENT_165_run_dialog_104_"),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
