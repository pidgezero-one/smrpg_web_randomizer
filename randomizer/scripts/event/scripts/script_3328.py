# E3328_VOLCANO_GENERIC_LOADER_1

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_3),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToObjectXY(MARIO),
                ASSet700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
                ASFaceEast7C(),
                ASPause(1),
            ],
        ),
        RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
        Return(),
    ]
)
