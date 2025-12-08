# pylint: disable=C0301

"""E2529_STAR_HILL_1ST_ROOM_WISH_TOP_LEFT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        RunDialog(
            dialog_id=DI3115_WISH_9,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        PlaySound(sound=SO000_SILENCE, channel=6),
        JmpIfBitSet(MALLOWS_WISH_READ, ["EVENT_2529_ret_25"]),
        SetBit(MALLOWS_WISH_READ),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_15),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASWalk1StepNortheast(),
                ASWalkNortheastPixels(4),
                ASFaceSouthwest(),
            ]),
        FreezeCamera(),
        Pause(8),
        ActionQueueSync(
            target=NPC_15,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASStartLoopNTimes(3),
                ASWalkSouthwestPixels(2),
                ASPause(8),
                ASEndLoop(),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASPause(8),
                ASStartLoopNTimes(3),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASWalkSouthwestPixels(2),
                ASEndLoop(),
                ASFaceNortheast(),
            ]),
        RunDialog(
            dialog_id=DI3120_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        StopEmbeddedActionScript(NPC_15),
        Pause(16),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueSync(
            target=NPC_15,
            subscript=[ASSetSpriteSequence(index=8, is_sequence=True, looping=True)]),
        RunDialog(
            dialog_id=DI3121_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False),
        PauseScriptResumeOnNextDialogPageB(),
        ActionQueueSync(
            target=NPC_15,
            subscript=[
                ASSetSpriteSequence(
                    index=9, sprite_offset=1, is_sequence=True, looping=True
                )
            ]),
        UnsyncDialog(),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASResetProperties(),
                ASPause(16),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(4),
                ASPause(8),
                ASSetPriority(0),
                ASPause(24),
                ASSetPriority(3),
                ASWalk1StepNortheast(),
                ASSetSpriteSequence(
                    index=4, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASFaceSouthwest(),
            ]),
        RunDialog(
            dialog_id=DI3122_MALLOW_WISH_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASResetProperties(),
                ASWalk1StepSouthwest(),
                ASPause(4),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromCurrentLevel(NPC_15),
        UnfreezeCamera(),
        Return(identifier="EVENT_2529_ret_25"),
    ]
)
