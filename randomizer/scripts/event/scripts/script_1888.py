# pylint: disable=C0301

"""E1888_ABYSS_AXEM_PIT_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ActionQueueSync(target=NPC_0, subscript=[ASShadowOff()]),
        ActionQueueSync(target=NPC_1, subscript=[ASShadowOff()]),
        SetBit(UNKNOWN_DIRECTIONAL_BIT_1),
        ClearBit(ABYSS_TRAMPOLINE_DIRECTIONAL_BIT),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            mod_id=0,
        ),
        JmpIfBitClear(
            ABYSS_FINAL_ROOM_TRAMPOLINE, ["EVENT_1888_fade_in_from_black_async_10"]
        ),
        JmpToSubroutine(["EVENT_1897_fade_in_from_black_sync_7"]),
        Jmp(["EVENT_1888_run_background_event_11"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_1888_fade_in_from_black_async_10"
        ),
        RunBackgroundEvent(
            event_id=E1899_ABYSS_AXEM_PIT_ROOM_FALL_,
            return_on_level_exit=True,
            identifier="EVENT_1888_run_background_event_11",
        ),
        Return(),
    ]
)
