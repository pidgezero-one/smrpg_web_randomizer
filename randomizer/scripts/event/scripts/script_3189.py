# E3189_FALL_TO_MINECART_ROOM_FROM_LOBBY

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            face_direction=SOUTH,
            x=4,
            y=57,
            z=15,
            run_entrance_event=True,
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Return(),
    ]
)
