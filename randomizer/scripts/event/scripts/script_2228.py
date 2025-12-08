# pylint: disable=C0301

"""E2228_KEEP_DARK_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            ["EVENT_2228_db_2"]),
        SetSyncActionScript(NPC_2, A1010_KEEP_DARK_ROOM_INIT_GOOMBA),
        Db(bytearray(b"\xfd\x8f\x02"), identifier="EVENT_2228_db_2"),
        PrioritySet(
            mainscreen=[LAYER_L3],
            subscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
            colour_math=[BACKGROUND, HALF_INTENSITY]),
        ActionQueueSync(target=NPC_1, subscript=[ASSequenceLoopingOn()]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASWalkSoutheastPixels(4),
                ASFaceNorthwest(),
                ASSetSequenceSpeed(FAST),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASWalkSouthwestPixels(3),
                ASWalkSoutheastPixels(1),
                ASFaceSouthwest(),
            ]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASWalkSouthwestPixels(3),
                ASWalkSoutheastPixels(1),
                ASFaceSouthwest(),
            ]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 27, ["EVENT_2228_fade_in_from_black_async_14"]
        ),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        SetBit(TEMP_7043_1),
        SetBit(TEMP_7043_2),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2228_fade_in_from_black_async_14"
        ),
        Return(),
    ]
)
