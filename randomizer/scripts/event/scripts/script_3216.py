# pylint: disable=C0301

"""E3216_SHIP_COIN_SNAKE_PUZZLE_TAIL_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO013_COIN, channel=6),
        PauseActionScript(MEM_70A8),
        DisableObjectTrigger(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASShiftZUpSteps(2),
                ASVisibilityOff(),
            ]),
        Inc(TEMP_70AF),
        JmpIfVarEqualsConst(TEMP_70AF, 16, ["EVENT_3216_set_action_script_sync_7"]),
        Return(),
        SetSyncActionScript(
            NPC_17,
            A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL,
            identifier="EVENT_3216_set_action_script_sync_7"),
        JmpIfBitSet(SHIP_COIN_PRIZE, ["EVENT_3216_ret_15"]),
        SetBit(SHIP_COIN_PRIZE),
        JmpToEvent(E0178_NPC_QUEST_1_CONTAINER),
        Return(identifier="EVENT_3216_ret_15"),
    ]
)
