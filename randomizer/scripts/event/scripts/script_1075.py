# pylint: disable=C0301

"""E1075_TOADOFSKY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2719_MUSIC_TUTORIAL_PROMPT,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_1075_run_dialog_27"]),
        SetBit(TEMP_7044_6),
        JmpToSubroutine(["EVENT_1078_jmp_if_bit_clear_140"]),
        RunDialog(
            dialog_id=DI2720_MUSIC_TUTORIAL,
            above_object=NPC_12,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False),
        Pause(1),
        PauseScriptResumeOnNextDialogPageB(),
        Pause(1),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=14, y=32, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASVisibilityOn(),
            ]),
        SetSyncActionScript(NPC_7, A0081_MELODY_BAY_TUTORIAL),
        PlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=6),
        Pause(1),
        PauseScriptResumeOnNextDialogPageB(),
        Pause(1),
        UnsyncDialog(),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkNorthwestSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO041_TADPOLE_POND_STAFF_LA, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkNorthwestSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO042_TADPOLE_POND_STAFF_TI, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(50),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASPause(45),
                ASWalkSoutheastSteps(2),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO040_TADPOLE_POND_STAFF_SO, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkSoutheastSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO039_TADPOLE_POND_STAFF_FA, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkSoutheastSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO038_TADPOLE_POND_STAFF_MI, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkSoutheastSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO037_TADPOLE_POND_STAFF_RE, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(25),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASVisibilityOff(),
                ASWalkSoutheastSteps(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(7),
                ASPlaySound(sound=SO036_TADPOLE_POND_STAFF_DO, channel=4),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(50),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASPause(10),
                ASVisibilityOff(),
            ]),
        CloseDialog(),
        RunDialog(
            dialog_id=DI2717_SONGS_FINISHED,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        ClearBit(TEMP_7044_6),
        Return(),
        RunDialog(
            dialog_id=DI2721_MUSIC_TUTORIAL_DECLINE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_1075_run_dialog_27"),
        Return(),
        RunDialog(
            dialog_id=DI2721_MUSIC_TUTORIAL_DECLINE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
