# pylint: disable=C0301

"""E1864_BOWSER_DOOR_ULTIMATE_FAILURE_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12, sprite_offset=2, is_sequence=True, looping=True
                )
            ],
        ),
        SlowDownMusic(identifier="EVENT_1864_slow_down_music_6"),
        Pause(90),
        FadeOutToBlack(sync=False, duration=40),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        Return(),
    ]
)
