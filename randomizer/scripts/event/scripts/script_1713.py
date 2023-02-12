# E1713_BANDITS_WAY_3_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_5),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        JmpIfBitClear(BANDITS_WAY_CUTSCENE_3_VIEWED, ["EVENT_1713_jmp_if_bit_clear_6"]),
        RunEventAsSubroutine(E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        Return(),
        JmpIfBitClear(
            UNKNOWN_7077_7,
            ["EVENT_1713_sequence_setter_3"],
            identifier="EVENT_1713_jmp_if_bit_clear_6",
        ),
        SetSyncActionScript(NPC_8, A0162_BOSS_IN_BANDITS_WAY_3),
        RunEventAsSubroutine(E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        Return(),
        RunEventAsSubroutine(
            E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_1713_sequence_setter_3",
        ),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(
                    index=5, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Pause(60),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(96),
                ASPause(30),
                ASResetProperties(),
                ASFaceSouthwest(),
            ],
        ),
        SetSyncActionScript(NPC_8, A0162_BOSS_IN_BANDITS_WAY_3),
        Return(),
    ]
)
