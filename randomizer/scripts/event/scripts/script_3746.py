# E3746_HOT_SPRINGS_TRAMPOLINE_TO_MEZZANINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(DIRECTIONAL_7049_0, ["EVENT_3746_run_event_as_subroutine_11"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE,
            face_direction=SOUTHWEST,
            x=28,
            y=17,
            z=0,
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=132, silent=True),
                ASShiftSouthwestSteps(2),
                ASFloatingOn(),
                ASShiftSouthwestPixels(20),
            ],
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
        PauseScriptUntilEffectDone(),
        Return(),
        RunEventAsSubroutine(
            E0065_TRAMPOLINE_SUBROUTINE,
            identifier="EVENT_3746_run_event_as_subroutine_11",
        ),
        Return(),
    ]
)
