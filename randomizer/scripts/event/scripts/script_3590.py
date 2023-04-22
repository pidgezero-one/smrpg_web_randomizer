# pylint: disable=C0301

"""E3590_ROSE_TOWN_CHIMNEY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(X_COORD_2, 23),
        SetVarToConst(Y_COORD_2, 47),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        EnterArea(
            room_id=R087_ROSE_TOWN_ITEM_SHOP, face_direction=SOUTH, x=7, y=69, z=3
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_3590_set_bit_7"]
        ),
        ActionQueueSync(target=NPC_5, subscript=[ASVisibilityOn()]),
        SetBit(TEMP_709C_3, identifier="EVENT_3590_set_bit_7"),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        RunEventAsSubroutine(E0282_UNKNOWN_PIPE_VAULT),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3590_pause_11"),
        JmpIfMarioInAir(["EVENT_3590_pause_11"]),
        StopSound(),
        PlaySound(sound=SO058_INSERT, channel=6),
        ClearBit(DIRECTIONAL_7049_0),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
