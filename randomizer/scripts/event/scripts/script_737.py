# pylint: disable=C0301

"""E0737_GARROS_HOUSE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PaletteSet(palette_set=110, row=1),
        SetVarToRandom(PRIMARY_TEMP_7000, 6),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_737_action_queue_async_9"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_737_set_action_script_sync_14"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_737_action_queue_async_11"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_737_set_action_script_sync_14"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_737_action_queue_async_13"]),
        Jmp(["EVENT_737_set_action_script_sync_14"]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                )
            ],
            identifier="EVENT_737_action_queue_async_9"),
        Jmp(["EVENT_737_set_action_script_sync_14"]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_mold=True, looping=True, mirror_sprite=True
                )
            ],
            identifier="EVENT_737_action_queue_async_11"),
        Jmp(["EVENT_737_set_action_script_sync_14"]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetSpriteSequence(
                    index=3, is_mold=True, looping=True, mirror_sprite=True
                )
            ],
            identifier="EVENT_737_action_queue_async_13"),
        SetSyncActionScript(
            NPC_0,
            A0119_SLOW_SEQUENCE_LOOP,
            identifier="EVENT_737_set_action_script_sync_14"),
        RunEventAsSubroutine(E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
