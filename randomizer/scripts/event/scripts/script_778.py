# E0778_MINES_LEFT_OF_TRAMPOLINE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0779_MINES_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASShiftWestPixels(2), ASFaceSouthwest(), ASSequenceLoopingOff()],
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
