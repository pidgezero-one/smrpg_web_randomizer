# pylint: disable=C0301

"""E3334_VOLCANO_ENTER_SHOP_AREA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0]),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ],
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 387, ["EVENT_3334_action_queue_async_11"]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASWalkToXYCoords(x=14, y=102),
                ASWalkNortheastSteps(2),
                ASVisibilityOff(),
            ],
        ),
        EnterArea(
            room_id=R353_VOLCANO_AREA_18_HINO_MART,
            face_direction=NORTHEAST,
            x=1,
            y=61,
            z=0,
            show_banner=True,
            run_entrance_event=True,
        ),
        Return(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASWalkToXYCoords(x=3, y=17),
                ASWalkNortheastSteps(2),
                ASVisibilityOff(),
            ],
            identifier="EVENT_3334_action_queue_async_11",
        ),
        EnterArea(
            room_id=R353_VOLCANO_AREA_18_HINO_MART,
            face_direction=NORTHEAST,
            x=6,
            y=71,
            z=0,
            show_banner=True,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
