# pylint: disable=C0301

"""E2050_MONSTRO_THWOMP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Inc(MONSTRO_THWOMP_COUNTER),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(1),
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(6),
                ASSetSpriteSequence(
                    index=2, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(15),
                ASSetWalkingSpeed(FAST),
                ASShiftZUpSteps(3),
                ASSetWalkingSpeed(FASTER),
                ASShiftZUpSteps(1),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZUpSteps(1),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(3),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftZDownSteps(2),
            ]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=108, silent=True)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASJumpToHeight(height=108, silent=True)]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASJumpToHeight(height=108, silent=True)]
        ),
        PlaySound(sound=SO073_THWOMP_STOMP, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(22),
                ASWalkNorthPixels(22),
                ASWalkSouthPixels(14),
                ASWalkNorthPixels(14),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
            ]),
        JmpIfVarEqualsConst(MONSTRO_THWOMP_COUNTER, 7, ["EVENT_2050_run_dialog_20"]),
        Return(),
        RunDialog(
            dialog_id=DI2963_THWOMP_MAXED,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_2050_run_dialog_20"),
        SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN),
        Return(),
    ]
)
