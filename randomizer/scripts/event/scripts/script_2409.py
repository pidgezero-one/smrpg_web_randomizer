# pylint: disable=C0301

"""E2409_ABYSS_ROOM_BEFORE_1ST_BOSS_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(FACTORY_FALL_1, 237, ["EVENT_2409_set_26"]),
        ActionQueueSync(
            target=NPC_4, subscript=[ASWalkSouthPixels(2), ASWalkSoutheastPixels(5)]
        ),
        ActionQueueSync(target=NPC_6, subscript=[ASWalkSouthwestPixels(12)]),
        SetVarToConst(FACTORY_FALL_1, 239),
        SetVarToConst(FACTORY_FALL_2, 24),
        SetVarToConst(FACTORY_FALL_3, 16),
        ClearBit(DIRECTIONAL_7045_0),
        FreezeCamera(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=25, y=44),
                ASWalkSouthwestPixels(5),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=25, y=43),
                ASWalkSouthwestPixels(11),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftToXYCoords(x=27, y=39),
                ASWalkSouthwestPixels(5),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=28, y=38),
                ASWalkSouthwestPixels(11),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=32, y=43, z=0, direction=EAST),
            ]),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_set_26"),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        ClearBit(DIRECTIONAL_7045_0),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftZDownPixels(19)]),
        ActionQueueSync(
            target=NPC_1, subscript=[ASWalkSouthwestPixels(6), ASShiftZDownPixels(19)]
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASShiftZDownPixels(19)]),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(6), ASShiftZDownPixels(19)]
        ),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_set_39"),
        SetVarToConst(FACTORY_FALL_2, 24),
        SetVarToConst(FACTORY_FALL_3, 16),
        ClearBit(DIRECTIONAL_7045_0),
        FreezeCamera(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=25, y=44),
                ASWalkSouthwestPixels(5),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=25, y=43),
                ASWalkSouthwestPixels(11),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftToXYCoords(x=27, y=39),
                ASWalkSouthwestPixels(5),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=28, y=38),
                ASWalkSouthwestPixels(11),
                ASShiftZDownPixels(19),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=27, y=43, z=0, direction=EAST),
            ]),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        Return(),
        SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_jmp_if_bit_clear_57"),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        ClearBit(DIRECTIONAL_7045_0),
        FreezeCamera(),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftZDownPixels(19)]),
        ActionQueueSync(
            target=NPC_1, subscript=[ASWalkSouthwestPixels(6), ASShiftZDownPixels(19)]
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASShiftZDownPixels(19)]),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkSouthwestPixels(6), ASShiftZDownPixels(19)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASOverwriteSolidity(),
                ASTransferToXYZF(x=20, y=60, z=0, direction=EAST),
            ]),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0860_ABYSS_BEFORE_1ST_BOSS_JUMP_BACK_UP),
        SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RunBackgroundEvent(
            event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
