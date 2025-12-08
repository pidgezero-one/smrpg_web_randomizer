# pylint: disable=C0301

"""E0439_PIPE_VAULT_FIREBALL_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        StartBattleAtBattlefield(30, BF21_KERO_SEWERS),
        RunEventAsSubroutine(E0440_PIPE_VAULT_FIREBALL_BACKGROUND),
        JmpIfBitSet(RUN_AWAY, ["EVENT_439_action_queue_async_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        ActionQueueAsync(
            target=MARIO, subscript=[ASTransferToXYZF(x=10, y=10, z=2, direction=EAST)]
        ),
        Jmp(["EVENT_439_jmp_if_bit_clear_8"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASTransferToXYZF(x=8, y=13, z=4, direction=EAST)],
            identifier="EVENT_439_action_queue_async_7"),
        JmpIfBitClear(
            RUN_AWAY,
            ["EVENT_439_fade_in_from_black_async_10"],
            identifier="EVENT_439_jmp_if_bit_clear_8"),
        SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False, identifier="EVENT_439_fade_in_from_black_async_10"),
        Jmp(["EVENT_436_action_queue_async_13"]),
    ]
)
