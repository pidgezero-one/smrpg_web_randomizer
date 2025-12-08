# pylint: disable=C0301

"""E2340_TOWER_SEESAW_CHEST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASWalkSouthwestPixels(5),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownPixels(4),
                ASWalkSouthPixels(6),
                ASWalkNortheastPixels(8),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(9),
            ]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        RunEventAsSubroutine(
            E0881_BOOSTER_PASS_SEESAW_CHEST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_2340_set_bit_7"]),
        FadeInFromBlack(sync=False),
        Return(),
        SetBit(TEMP_7043_1, identifier="EVENT_2340_set_bit_7"),
        RunBackgroundEvent(
            event_id=E2343_TOWER_SEESAW_ROOM_SET_ORIGIN,
            return_on_level_exit=True,
            bit_6=True),
        RunBackgroundEvent(
            event_id=E2358_TOWER_THWOMP_SEESAW_ROOM_LOADER_CONTD,
            return_on_level_exit=True,
            bit_7=True),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
