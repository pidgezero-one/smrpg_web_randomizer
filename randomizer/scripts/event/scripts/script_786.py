# E0786_MINES_LONG_ROOM_IN_MINIBOSS_PATH_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0787_MINES_LONG_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftNortheastPixels(4),
                ASFaceSoutheast(),
                ASSequenceLoopingOff(),
            ],
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
