# pylint: disable=C0301

"""E2531_STAR_HILL_2ND_ROOM_WISH_BOTTOM_RIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_2531_run_dialog_5"]),
        RunDialog(
            dialog_id=DI3327_CONVERTED_WISH,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Return(),
        RunDialog(
            dialog_id=DI3116_WISH_10,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_2531_run_dialog_5",
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        JmpIfBitSet(MALLOWS_PARENTS_WISH_READ, ["EVENT_2531_ret_38"]),
        SetBit(MALLOWS_PARENTS_WISH_READ),
        FadeOutMusicFDA3(),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_21),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASJumpToHeight(108),
                ASWalk1StepNortheast(),
                ASWalkNortheastPixels(8),
            ],
        ),
        RunDialog(
            dialog_id=DI3123_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        PauseScriptResumeOnNextDialogPageB(),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNortheast()]),
        PauseScriptResumeOnNextDialogPageB(),
        PlayMusicAtDefaultVolume(M21_SAD_SONG),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[ASSetSpriteSequence(index=6, is_sequence=True, looping=True)],
        ),
        UnsyncDialog(),
        Pause(48),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        Pause(48),
        RunDialog(
            dialog_id=DI3126_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASStartLoopNTimes(8),
                ASWalkNorthPixels(1),
                ASPause(2),
                ASWalkSouthPixels(1),
                ASPause(16),
                ASEndLoop(),
            ],
        ),
        UnsyncDialog(),
        Pause(96),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        RunDialog(
            dialog_id=DI3124_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Pause(16),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(32),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[
                ASSetSpriteSequence(
                    index=9, sprite_offset=1, is_sequence=True, looping=True
                )
            ],
        ),
        RunDialog(
            dialog_id=DI3125_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_21,
            subscript=[
                ASResetProperties(),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(8),
                ASVisibilityOff(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_21),
        FadeOutMusicFDA3(),
        Pause(16),
        PlayMusicAtDefaultVolume(M34_STAR_HILL),
        Return(identifier="EVENT_2531_ret_38"),
    ]
)
