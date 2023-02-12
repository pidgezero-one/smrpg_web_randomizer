# E3780_BEAN_VALLEY_2ND_VINE_ROOM_EXIT_TO_EAST_VINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnterArea(
            room_id=R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02,
            face_direction=SOUTHEAST,
            x=25,
            y=114,
            z=0,
        ),
        Db(bytearray(b"\xfdI")),
        JmpToSubroutine(["EVENT_3780_jmp_if_present_in_current_level_9"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASShiftSoutheastSteps(2),
                ASSetSolidityBits(cant_pass_walls=True),
                ASShiftSoutheastPixels(20),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3780_pause_6"),
        JmpIfMarioInAir(["EVENT_3780_pause_6"]),
        Return(),
        JmpIfObjectInCurrentLevel(
            NPC_3,
            ["EVENT_3780_jmp_if_present_in_current_level_11"],
            identifier="EVENT_3780_jmp_if_present_in_current_level_9",
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASTransferXYZFPixels(x=6, y=254, z=0, direction=EAST)],
        ),
        JmpIfObjectInCurrentLevel(
            NPC_4,
            ["EVENT_3780_jmp_if_present_in_current_level_13"],
            identifier="EVENT_3780_jmp_if_present_in_current_level_11",
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASTransferXYZFPixels(x=6, y=254, z=0, direction=EAST)],
        ),
        JmpIfObjectInCurrentLevel(
            NPC_5,
            ["EVENT_3780_jmp_if_present_in_current_level_15"],
            identifier="EVENT_3780_jmp_if_present_in_current_level_13",
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASTransferXYZFPixels(x=6, y=254, z=0, direction=EAST)],
        ),
        JmpIfObjectInCurrentLevel(
            NPC_6,
            ["EVENT_3780_jmp_if_present_in_current_level_17"],
            identifier="EVENT_3780_jmp_if_present_in_current_level_15",
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASTransferXYZFPixels(x=6, y=254, z=0, direction=EAST)],
        ),
        JmpIfObjectInCurrentLevel(
            NPC_7,
            ["EVENT_3780_action_queue_sync_19"],
            identifier="EVENT_3780_jmp_if_present_in_current_level_17",
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASTransferXYZFPixels(x=6, y=254, z=0, direction=EAST)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)],
            identifier="EVENT_3780_action_queue_sync_19",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02,
            ["EVENT_3780_ret_23"],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST),
                ASShadowOff(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        Return(identifier="EVENT_3780_ret_23"),
    ]
)
