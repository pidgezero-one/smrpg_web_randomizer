# E2081_MUSTY_FEARS_LAMP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TIMER_7022, 8),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(2),
                ASSetSpriteSequence(
                    index=12, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=13, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        SetVarToConst(ITEM_ID, BigBooFlag),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_1"]
        ),
        SetVarToConst(ITEM_ID, DryBonesFlag),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_1"]
        ),
        SetVarToConst(ITEM_ID, GreaperFlag),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_1"]
        ),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        RemoveOneOfItemFromInventory(BigBooFlag),
        RemoveOneOfItemFromInventory(DryBonesFlag),
        RemoveOneOfItemFromInventory(GreaperFlag),
        Jmp(["EVENT_2081_action_queue_async_2_"]),
        RunBackgroundEventWithPause(
            event_id=E3075_HEAL_FLASH,
            timer_var=TIMER_7022,
            identifier="EVENT_2081_run_background_event_with_pause_1",
        ),
        PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
        RestoreAllHP(),
        RestoreAllFP(),
        Pause(60),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASResetProperties()],
            identifier="EVENT_2081_action_queue_async_2_",
        ),
        Return(),
    ]
)
