# pylint: disable=C0301

"""E3142_PIPE_TO_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 12),
        SetVarToConst(Y_COORD_2, 108),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        JmpIfBitSet(SEWER_BOSS_DEFEATED, ["EVENT_3142_set_bit_14"]),
        EnterArea(
            room_id=R302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            face_direction=NORTHEAST,
            x=6,
            y=40,
            z=9),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceNortheast(), ASJumpToHeight(height=0, silent=True)]),
        ActionQueueSync(target=NPC_3, subscript=[ASShadowOff()]),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftSouthSteps(6),
                ASSetWalkingSpeed(NORMAL),
            ]),
        Pause(1, identifier="EVENT_3142_pause_11"),
        JmpIfMarioInAir(["EVENT_3142_pause_11"]),
        Return(),
        SetBit(UNKNOWN_MIDAS_RIVER_704D_6, identifier="EVENT_3142_set_bit_14"),
        ClearBit(BUCKET_WARP_BIT),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL,
            face_direction=SOUTH,
            x=9,
            y=108,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
