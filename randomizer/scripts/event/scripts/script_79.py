# pylint: disable=C0301

"""E0079_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        Db(bytearray(b"\xfdD")),
        Db(bytearray(b"\xfdE")),
        Db(bytearray(b"\xfdG")),
        RunEventAtReturn(E0078_UNKNOWN),
        Return(),
    ]
)
