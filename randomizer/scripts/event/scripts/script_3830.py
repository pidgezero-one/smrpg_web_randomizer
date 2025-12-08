# pylint: disable=C0301

"""E3830_MUSHROOM_KINGDOM_SHOP_CELLAR_NPC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_3830_run_dialog_14"]),
        RunDialog(
            dialog_id=DI3747_TALK_TO_NPCS_AGAIN_HINT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        RunDialog(
            dialog_id=DI3746_RARE_FROG_COIN_HINT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3830_run_dialog_14"),
        Return(),
    ]
)
