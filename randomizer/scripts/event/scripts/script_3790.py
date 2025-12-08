# pylint: disable=C0301

"""E3790_BEAN_VALLEY_2ND_VINE_ROOM_EXIT_TO_WEST_VINE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnterArea(
            room_id=R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
            face_direction=NORTHWEST,
            x=16,
            y=84,
            z=0),
        Db(bytearray(b"\xfdI")),
        JmpToSubroutine(["EVENT_3790_jmp_if_present_in_current_level_9"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASWalkNorthwestSteps(2),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalkNorthwestPixels(20),
                ASSetWalkingSpeed(NORMAL),
            ]),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3790_pause_6"),
        JmpIfMarioInAir(["EVENT_3790_pause_6"]),
        Return(),
        JmpIfObjectInCurrentLevel(
            NPC_3,
            ["EVENT_3790_jmp_if_present_in_current_level_11"],
            identifier="EVENT_3790_jmp_if_present_in_current_level_9"),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)]),
        JmpIfObjectInCurrentLevel(
            NPC_4,
            ["EVENT_3790_jmp_if_present_in_current_level_13"],
            identifier="EVENT_3790_jmp_if_present_in_current_level_11"),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)]),
        JmpIfObjectInCurrentLevel(
            NPC_5,
            ["EVENT_3790_jmp_if_present_in_current_level_15"],
            identifier="EVENT_3790_jmp_if_present_in_current_level_13"),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)]),
        JmpIfObjectInCurrentLevel(
            NPC_6,
            ["EVENT_3790_jmp_if_present_in_current_level_17"],
            identifier="EVENT_3790_jmp_if_present_in_current_level_15"),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)]),
        JmpIfObjectInCurrentLevel(
            NPC_7,
            ["EVENT_3790_remember_last_object_19"],
            identifier="EVENT_3790_jmp_if_present_in_current_level_17"),
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)]),
        RememberLastObject(identifier="EVENT_3790_remember_last_object_19"),
        Return(),
    ]
)
