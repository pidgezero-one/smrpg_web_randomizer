# pylint: disable=C0301

"""E0503_PIPE_VAULT_CROUCH_ITEM_CONFIRM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_0, ["EVENT_256_ret_0"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        Set7000ToPressedButton(),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_503_start_loop_n_times_5"]),
        Return(),
        StartLoopNTimes(7, identifier="EVENT_503_start_loop_n_times_5"),
        Set7000ToPressedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_503_remember_last_object_20"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_503_enable_controls_until_return_12"]
        ),
        Pause(1),
        EndLoop(),
        Return(),
        EnableControlsUntilReturn(
            [], identifier="EVENT_503_enable_controls_until_return_12"
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetSpriteSequence(
                    index=16,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepNortheast(),
                ASSetWalkingSpeed(SLOW),
                ASWalkNortheastPixels(8),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkNortheastPixels(4),
                ASSetWalkingSpeed(NORMAL),
                ASWalkToXYCoords(x=8, y=64),
            ]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_503_remember_last_object_20"]),
        Pause(10),
        SetVarToConst(ACTIVE_NPC, 25),
        RunEventAsSubroutine(E0236_FREESTANDING_6_GRANT),
        RememberLastObject(identifier="EVENT_503_remember_last_object_20"),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
