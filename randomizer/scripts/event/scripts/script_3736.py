# E3736_NIMBUS_CASTLE_FINAL_HALLWAY_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            ["EVENT_3736_fade_in_from_black_async_3"],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferXYZFPixels(x=252, y=252, z=0, direction=EAST),
                ASFaceNortheast(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        RunBackgroundEvent(
            event_id=E3735_NIMBUS_CASTLE_FINAL_HALLWAY_APPLY_MOD,
            return_on_level_exit=True,
        ),
        RunEventAsSubroutine(
            E0820_NIMBUS_CASTLE_FINAL_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_3736_fade_in_from_black_async_3"),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_3584_ret_0"]),
        SetVarToConst(TIMER_7022, 70),
        ClearBit(EXP_STAR_BIT_6),
        CreatePacketAtObjectCoords(
            packet=P022_RECURSIVE_SPARKLES,
            object=MARIO,
            destinations=["EVENT_3584_ret_0"],
        ),
        Return(),
    ]
)
