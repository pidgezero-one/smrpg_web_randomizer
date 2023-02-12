# E3298_SEA_REVERSE_WHIRLPOOL_TO_LONE_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASStartLoopNTimes(31),
                ASTurnClockwise45DegreesNTimes(1),
                ASShiftZUpPixels(2),
                ASEndLoop(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        Pause(50),
        EnterArea(
            room_id=R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
            face_direction=SOUTH,
            x=23,
            y=33,
            z=7,
            run_entrance_event=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(7),
                ASTurnClockwise45DegreesNTimes(1),
                ASShiftZUpPixels(2),
                ASEndLoop(),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        Return(),
    ]
)
