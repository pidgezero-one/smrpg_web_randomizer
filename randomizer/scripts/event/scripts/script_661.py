# pylint: disable=C0301

"""E0661_BOWSERS_KEEP_BUTTON_ROOM_FORFEIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2888_DR_TOPPER_PROMPT_TO_QUIT_BUTTON_PUZZLE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_661_play_sound_168"]),
        Jmp(["EVENT_661_action_queue_async_2_"]),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_661_play_sound_168"
        ),
        Pause(16),
        SetBit(TEMP_7044_7),
        PlayMusicAtDefaultVolume(M66_BOWSERS_CASTLE_2ND_TIME),
        SlowDownMusic(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(2),
            ],
        ),
        Pause(180),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASWalkToXYCoords(x=23, y=31)],
            identifier="EVENT_661_action_queue_async_2_",
        ),
        Return(),
    ]
)
