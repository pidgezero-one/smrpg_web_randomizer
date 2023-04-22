# pylint: disable=C0301

"""E0080_SAVE_BLOCK_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseScriptIfMenuOpen(),
        JmpIfBitSet(TEMP_7076_0, ["EVENT_81_ret_9"]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_256_ret_0"]),
        SetBit(MONSTRO_SAVE_HOLE),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70C6),
        EnableControlsUntilReturn([]),
        FreezeCamera(),
        UnfreezeAllNPCs(),
        PlaySound(sound=SO150_EXIT_TO_WORLD_MAP, channel=6),
        SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSequencePlaybackOff(),
                ASSetPriority(3),
                ASSetWalkingSpeed(FASTEST),
                ASShadowOff(),
                ASShiftZUpSteps(14),
                ASCopyVarToVar(from_var=UNKNOWN_70C6, to_var=PRIMARY_TEMP_700C),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
                ASDb(bytearray(b"\xc8\x91")),
                ASWalkTo70167018(),
                ASReturn(),
            ],
        ),
        FadeOutToBlack(sync=False),
        OpenSaveMenu(),
    ]
)
