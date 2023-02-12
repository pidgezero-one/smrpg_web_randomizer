# E3697_NIMBUS_CASTLE_WEST_LOWER_HALL_PINWHEEL_ANIMATIONS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(120),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
            ],
        ),
        SetBit(TEMP_7043_0),
        SetSyncActionScript(MARIO, A0809_MARIO_BLOWN_BY_FAN),
        Pause(240),
        ClearBit(TEMP_7043_0),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASSetSequenceSpeed(SLOW), ASResetProperties()]
        ),
        SetSyncActionScript(MARIO, A0814_MARIO_BLOWN_BY_FAN),
        JmpToEvent(E3697_NIMBUS_CASTLE_WEST_LOWER_HALL_PINWHEEL_ANIMATIONS),
    ]
)
