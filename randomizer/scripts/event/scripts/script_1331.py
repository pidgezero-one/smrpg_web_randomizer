# pylint: disable=C0301

"""E1331_TOWER_BREAK_DOWN_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TOWER_OPENED, ["EVENT_1331_ret"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["EVENT_1331_ret"]),
        RemoveObjectFromCurrentLevel(NPC_1),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=4, y=114),
                ASFaceEast(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        Pause(25),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_0),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASWalkToXYCoords(x=5, y=115),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(15),
                ASFaceSouthwest(),
                ASPause(15),
                ASSetSequenceSpeed(SLOW),
                ASSequenceLoopingOn(),
                ASPause(15),
                ASSetSequenceSpeed(NORMAL),
                ASPause(15),
                ASSetSequenceSpeed(FAST),
                ASPause(15),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(45),
                ASSetWalkingSpeed(VERY_FAST),
                ASFixedFCoordOn(),
                ASWalkNortheastSteps(2),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSequenceLoopingOff(),
                ASSequencePlaybackOff(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkNortheastPixels(18),
                ASWalkSouthwestPixels(12),
                ASWalkNortheastPixels(8),
                ASWalkSouthwestPixels(6),
                ASWalkNortheastPixels(4),
                ASWalkSouthwestPixels(4),
            ],
        ),
        Pause(5),
        ApplySolidityModToLevel(
            permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=32
        ),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromSpecificLevel(NPC_2, R202_BOOSTER_TOWER_ENTRANCE),
        Pause(60),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=10, sprite_offset=1, is_sequence=True, looping=False
                ),
                ASPause(60),
                ASResetProperties(),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASWalkToXYCoords(x=5, y=116), ASFaceNortheast()]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOff(),
                ASSequenceLoopingOn(),
                ASSequencePlaybackOn(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(NORMAL),
                ASWalkToXYCoords(x=5, y=116),
                ASVisibilityOff(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        SetBit(TOWER_OPENED),
        Return(identifier="EVENT_1331_ret"),
    ]
)
