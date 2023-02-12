# E3724_NIMBUS_CASTLE_OUTER_CELLAR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3724_jmp_if_bit_set_5"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=28,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(1),
                ASResetProperties(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_3724_run_event_as_subroutine_8"],
            identifier="EVENT_3724_jmp_if_bit_set_5",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_3724_run_event_as_subroutine_8",
        ),
        Return(),
    ]
)
