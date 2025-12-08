# pylint: disable=C0301

"""E2308_BOOSTER_PASS_1ST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(NPC_0, R100_BOOSTER_PASS_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_1, R100_BOOSTER_PASS_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_2, R100_BOOSTER_PASS_AREA_01),
        RunBackgroundEvent(
            event_id=E2309_BOOSTER_PASS_LAKITU_TOSSES_SPINY, return_on_level_exit=True
        ),
        JmpIfBitClear(
            DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING,
            ["EVENT_2308_fade_in_from_black_async_26"]),
        ActionQueueAsync(target=MARIO, subscript=[ASFloatingOff()]),
        RemoveObjectFromCurrentLevel(MARIO),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(MARIO, A0397_PLAYER_TUMBLES_DOWN_BOOSTER_PASS),
        Pause(64),
        SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest()]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ClearBit(TEMP_7043_0),
        Return(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2308_fade_in_from_black_async_26"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2308_ret_38"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2308_ret_38"]),
        RunEventAsSubroutine(E3898_BOOSTER_PASS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2308_ret_38"),
    ]
)
