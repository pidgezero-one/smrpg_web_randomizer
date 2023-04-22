# pylint: disable=C0301

"""E3231_SHIP_CANNONBALL_PUZZLE_INITIATOR_BLOCK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(MEM_70A8),
        DisableObjectTrigger(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSetPaletteRow(2),
                ASDb(bytearray(b"\xfd\x9c\x05")),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x03\x80\xff")),
                ASPause(8),
                ASDb(bytearray(b"%@\x00\x80\xff")),
                ASPause(8),
                ASBPL262728(),
                ASSetPaletteRow(1),
                ASReturn(),
            ],
        ),
        SetSyncActionScript(NPC_4, A0319_SHIP_CANNONBALL_PUZZLE_CANNONBALL),
        Return(),
    ]
)
