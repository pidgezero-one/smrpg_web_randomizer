# pylint: disable=C0301

"""E2564_BOOSTER_PASS_BUSH_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BOOSTER_PASS_BUSH_ITEM_FOUND, ["EVENT_2564_ret_6"]),
        RunDialog(
            dialog_id=DI3156_BOOSTER_PASS_BUSH,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetBit(BOOSTER_PASS_BUSH_ITEM_FOUND),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(identifier="EVENT_2564_ret_6"),
    ]
)
