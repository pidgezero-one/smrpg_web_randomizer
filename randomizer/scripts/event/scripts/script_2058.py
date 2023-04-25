# pylint: disable=C0301

"""E2058_MONSTRO_FAN_SETTING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2987_FAN_SETTING,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_2058_action_queue_async_4", "EVENT_2058_action_queue_async_6"]
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPause(5),
                ASPlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Return(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPause(5),
                ASPlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
            identifier="EVENT_2058_action_queue_async_4",
        ),
        Return(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPause(5),
                ASPlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=3, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
            identifier="EVENT_2058_action_queue_async_6",
        ),
        Return(),
    ]
)
