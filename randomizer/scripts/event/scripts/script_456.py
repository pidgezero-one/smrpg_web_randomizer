# pylint: disable=C0301

"""E0456_YOSHI_TALKS_TO_OTHER_YOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([]),
        SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
        Db(bytearray(b"\xfdE")),
        Return(),
    ]
)
