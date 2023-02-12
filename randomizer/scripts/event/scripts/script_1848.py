# E1848_CANNONBALL_ROOM_BOMB_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIf316DIs3(["EVENT_1848_enable_controls_10"]),
        FreezeAllNPCsUntilReturn(),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASPlaySound(sound=SO089_LIT_FUSE, channel=4),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(30),
            ],
        ),
        Pause(1, identifier="EVENT_1848_pause_5"),
        CreatePacketAtObjectCoords(
            packet=P024_REGULAR_SOUND_EXPLOSION,
            object=NPC_2,
            destinations=["EVENT_1848_pause_5"],
        ),
        PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=6),
        RemoveObjectFromCurrentLevel(NPC_2),
        Jmp(["EVENT_1847_action_queue_async_9"]),
        EnableControls([], identifier="EVENT_1848_enable_controls_10"),
        RunBackgroundEvent(
            event_id=E1850_CANNONBALL_ROOM_BOMB_2_CONTD, return_on_level_exit=True
        ),
        Return(),
    ]
)
