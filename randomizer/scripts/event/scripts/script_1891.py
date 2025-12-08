# pylint: disable=C0301

"""E1891_ABYSS_BIG_CONVEYOR_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        SetBit(ABYSS_TRAMPOLINE_DIRECTIONAL_BIT),
        ApplyTileModToLevel(
            use_alternate=False,
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            mod_id=0),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            mod_id=0),
        JmpIfBitClear(
            ABYSS_FINAL_ROOM_TRAMPOLINE, ["EVENT_1891_fade_in_from_black_async_7"]
        ),
        JmpToSubroutine(["EVENT_1897_fade_in_from_black_sync_7"]),
        Jmp(["EVENT_1891_run_background_event_8"]),
        FadeInFromBlack(sync=False, identifier="EVENT_1891_fade_in_from_black_async_7"),
        RunBackgroundEvent(
            event_id=E1900_ABYSS_BIG_CONVEYOR_ROOM_FALL,
            return_on_level_exit=True,
            identifier="EVENT_1891_run_background_event_8"),
        Return(),
    ]
)
