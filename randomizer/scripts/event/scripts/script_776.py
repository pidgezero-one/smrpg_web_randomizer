# E0776_MINES_TRAMPOLINE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0777_MINES_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftSouthPixels(4),
                ASFaceSouthwest(),
                ASSequenceLoopingOff(),
            ],
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
