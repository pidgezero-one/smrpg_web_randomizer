# E0437_PIPE_VAULT_FIREBALL_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        StartBattleAtBattlefield(31, BF21_KERO_SEWERS),
        RunEventAsSubroutine(E0440_PIPE_VAULT_FIREBALL_BACKGROUND),
        JmpIfBitSet(RUN_AWAY, ["EVENT_437_action_queue_async_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        ActionQueueAsync(
            target=MARIO, subscript=[ASTransferToXYZF(x=7, y=16, z=2, direction=EAST)]
        ),
        Jmp(["EVENT_437_set_bit_8"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASTransferToXYZF(x=5, y=19, z=4, direction=EAST)],
            identifier="EVENT_437_action_queue_async_7",
        ),
        SetBit(TEMP_7049_6, identifier="EVENT_437_set_bit_8"),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        JmpIfBitClear(RUN_AWAY, ["EVENT_437_fade_in_from_black_async_12"]),
        SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False, identifier="EVENT_437_fade_in_from_black_async_12"),
        Jmp(["EVENT_436_action_queue_async_13"]),
    ]
)
