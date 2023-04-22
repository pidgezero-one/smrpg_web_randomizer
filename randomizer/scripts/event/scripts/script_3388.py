# pylint: disable=C0301

"""E3388_SHIP_BOSS_ROOM_PERISCOPE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(JOHNNY_POSITION, ["EVENT_3388_ret_64"]),
        EnterArea(
            room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            face_direction=SOUTH,
            x=7,
            y=82,
            z=0,
        ),
        ActionQueueAsync(target=NPC_0, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_1, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_2, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_3, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_4, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_5, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_6, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_12, subscript=[ASVisibilityOff()]),
        RunEventAsSubroutine(E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED),
        JmpIfComparisonResultIsLesser(["EVENT_3388_action_queue_sync_14"]),
        ActionQueueAsync(target=NPC_14, subscript=[ASVisibilityOn()]),
        Jmp(["EVENT_3388_remove_from_current_level_50"]),
        ActionQueueAsync(
            target=NPC_14,
            subscript=[ASVisibilityOff()],
            identifier="EVENT_3388_action_queue_sync_14",
        ),
        RemoveObjectFromCurrentLevel(
            MARIO, identifier="EVENT_3388_remove_from_current_level_50"
        ),
        CircleMaskShrinkToObject(target=MARIO, width=96, speed=8, static=True),
        RunDialog(
            dialog_id=DI2266_EMPTY,
            above_object=Bowser,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        Pause(180),
        Pause(180),
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=8, static=True),
        EnterArea(
            room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            face_direction=NORTHEAST,
            x=24,
            y=110,
            z=0,
        ),
        RunEventAsSubroutine(E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        ActionQueueAsync(target=MARIO, subscript=[ASWalkNortheastPixels(4)]),
        FadeInFromBlack(sync=False),
        Return(identifier="EVENT_3388_ret_64"),
    ]
)
