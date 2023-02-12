# E2806_FOREST_MAZE_ROOM_BEFORE_TRUNK_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2806_fade_in_from_black_async_14"]),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(24),
        UnfreezeCamera(),
        Jmp(["EVENT_2806_ret_20"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2806_fade_in_from_black_async_14"
        ),
        Return(identifier="EVENT_2806_ret_20"),
    ]
)
