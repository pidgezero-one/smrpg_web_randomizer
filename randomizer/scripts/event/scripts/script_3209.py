# E3209_SLEEPING_DRY_BONES

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        RunDialog(
            dialog_id=DI1656_SLEEPING_DRY_BONES,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASTurnClockwise45DegreesNTimes(4),
                ASWalk1StepFDirection(),
                ASTurnClockwise45DegreesNTimes(4),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[ASSetSpriteSequence(index=8, looping=False), ASPause(36)],
        ),
        SetVarToConst(BATTLE_PACK_ID, 72),
        JmpToEvent(E0016_FIGHT_REMOVE_PERMANENTLY),
    ]
)
