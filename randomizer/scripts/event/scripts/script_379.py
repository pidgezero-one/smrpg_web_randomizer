# pylint: disable=C0301

"""E0379_MUSHROOM_KINGDOM_OCCUPIED_GUEST_ROOM_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED,
            ["EVENT_379_run_dialog_20"],
        ),
        SetBit(OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
        RunDialog(
            dialog_id=DI0655_VAULT_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_379_run_dialog_20",
        ),
        Return(),
    ]
)
