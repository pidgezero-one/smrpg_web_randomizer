# pylint: disable=C0301

"""E2362_ABYSS_FOUR_BOLT_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 19, ["EVENT_2362_set_21"]),
        SetVarToConst(FACTORY_FALL_1, 222),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        SetVarToConst(FACTORY_FALL_4, 0),
        SetVarToConst(FACTORY_FALL_5, 0),
        SetVarToConst(FACTORY_FALL_6, 0),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        ActionQueueSync(
            target=NPC_0, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_21"),
        SetVarToConst(FACTORY_FALL_2, 24),
        SetVarToConst(FACTORY_FALL_3, 30),
        SetVarToConst(FACTORY_FALL_4, 24),
        SetVarToConst(FACTORY_FALL_5, 16),
        SetVarToConst(FACTORY_FALL_6, 16),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=7, y=116), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=117),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASShiftToXYCoords(x=13, y=104), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=12, y=105),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASShiftToXYCoords(x=18, y=114), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShiftToXYCoords(x=17, y=115),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASShiftToXYCoords(x=11, y=118),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(2),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASShiftToXYCoords(x=11, y=119),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(8),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASShiftToXYCoords(x=17, y=107),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(5),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASShiftToXYCoords(x=17, y=106),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkSoutheastPixels(2),
                ASShiftZDownPixels(15),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_40"),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        SetVarToConst(FACTORY_FALL_4, 0),
        SetVarToConst(FACTORY_FALL_5, 0),
        SetVarToConst(FACTORY_FALL_6, 0),
        ActionQueueSync(
            target=NPC_0, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=7, y=130, z=0, direction=EAST),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        ClearBit(DIRECTIONAL_7045_7),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_66"),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 30),
        SetVarToConst(FACTORY_FALL_4, 0),
        SetVarToConst(FACTORY_FALL_5, 0),
        SetVarToConst(FACTORY_FALL_6, 0),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=7, y=116), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=117),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=12, y=118, z=0, direction=EAST),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        ClearBit(DIRECTIONAL_7045_7),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_92"),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 30),
        SetVarToConst(FACTORY_FALL_4, 0),
        SetVarToConst(FACTORY_FALL_5, 16),
        SetVarToConst(FACTORY_FALL_6, 0),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=7, y=116), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=117),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASShiftToXYCoords(x=11, y=118),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(2),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASShiftToXYCoords(x=11, y=119),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(8),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=16, y=127, z=0, direction=EAST),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        ClearBit(DIRECTIONAL_7045_7),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_118"),
        SetVarToConst(FACTORY_FALL_2, 24),
        SetVarToConst(FACTORY_FALL_3, 30),
        SetVarToConst(FACTORY_FALL_4, 0),
        SetVarToConst(FACTORY_FALL_5, 0),
        SetVarToConst(FACTORY_FALL_6, 0),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=7, y=116), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=117),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASShiftToXYCoords(x=13, y=104), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=12, y=105),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthwestPixels(4), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASWalkSouthwestPixels(10), ASShiftZDownPixels(11)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(7),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(13),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=18, y=106, z=0, direction=EAST),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        ClearBit(DIRECTIONAL_7045_7),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_144"),
        SetVarToConst(FACTORY_FALL_2, 24),
        SetVarToConst(FACTORY_FALL_3, 30),
        SetVarToConst(FACTORY_FALL_4, 24),
        SetVarToConst(FACTORY_FALL_5, 16),
        SetVarToConst(FACTORY_FALL_6, 16),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=7, y=116), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=117),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASShiftToXYCoords(x=13, y=104), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=12, y=105),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASShiftToXYCoords(x=18, y=114), ASShiftZDownPixels(11)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShiftToXYCoords(x=17, y=115),
                ASWalkNortheastPixels(6),
                ASShiftZDownPixels(11),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASShiftToXYCoords(x=11, y=118),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(2),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASShiftToXYCoords(x=11, y=119),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(8),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASShiftToXYCoords(x=17, y=107),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNorthwestPixels(5),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASShiftToXYCoords(x=17, y=106),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkSoutheastPixels(2),
                ASShiftZDownPixels(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=17, y=117, z=0, direction=EAST),
            ],
        ),
        FreezeCamera(),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        ClearBit(DIRECTIONAL_7045_7),
        Return(),
    ]
)
