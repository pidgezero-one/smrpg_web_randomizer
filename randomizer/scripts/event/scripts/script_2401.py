# pylint: disable=C0301

"""E2401_BEGIN_8BIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        JmpIfBitSet(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2401_ret_11"]),
        SetBit(TOWER_8BIT_EASTER_EGG_BIT_1),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=22, y=61),
                ASSetPriority(0),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASSetWalkingSpeed(SLOW),
            ],
        ),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_0),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]), ASShadowOff()],
        ),
        SummonObjectToCurrentLevel(NPC_1),
        SummonObjectToCurrentLevel(NPC_2),
        SummonObjectToCurrentLevel(NPC_3),
        SummonObjectToCurrentLevel(NPC_4),
        UnfreezeCamera(),
        RunBackgroundEvent(event_id=E2402_8BIT_BACKGROUND, return_on_level_exit=True),
        Return(identifier="EVENT_2401_ret_11"),
    ]
)
