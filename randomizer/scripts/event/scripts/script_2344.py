# E2344_TOWER_THWOMP_SEESAW_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_0, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
        SummonObjectToSpecificLevel(NPC_1, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
        SummonObjectToSpecificLevel(NPC_2, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftSouthwestPixels(12),
                ASShiftSoutheastPixels(2),
                ASShiftNorthPixels(1),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownPixels(4),
                ASShiftNorthPixels(15),
                ASShiftSoutheastPixels(5),
                ASShiftSouthwestPixels(5),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        Set7000ToObjectCoord(object=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_2344_freeze_camera_9"]),
        FadeInFromBlack(sync=False),
        Return(),
        FreezeCamera(identifier="EVENT_2344_freeze_camera_9"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftToXYCoords(x=4, y=110),
                ASShiftZUpSteps(16),
            ],
        ),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_2344_action_queue_async_13_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2344_action_queue_async_13_SUBSCRIPT_pause_1"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        UnfreezeCamera(),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
