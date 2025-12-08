# pylint: disable=C0301

"""E0164_NPC_QUEST_GRANT_STAR_PIECE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO081_STAR, channel=6),
        RunDialog(
            dialog_id=DI3079_GOT_A_STAR_PIECE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpToEvent(E3092_STAR_PIECE_GRANT),
    ]
)
