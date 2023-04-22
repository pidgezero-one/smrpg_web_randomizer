# pylint: disable=C0301

"""E2424_FOREST_ARROW_HITS_YOU"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 246, ["EVENT_2424_disable_trigger_4"]),
        DisableObjectTrigger(NPC_1),
        Jmp(["EVENT_2424_unfreeze_all_npcs_5"]),
        DisableObjectTrigger(NPC_13, identifier="EVENT_2424_disable_trigger_4"),
        UnfreezeAllNPCs(identifier="EVENT_2424_unfreeze_all_npcs_5"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSouthwest(),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        Pause(112),
        SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 246, ["EVENT_2424_enable_trigger_14"]),
        EnableObjectTrigger(NPC_1),
        Return(),
        EnableObjectTrigger(NPC_13, identifier="EVENT_2424_enable_trigger_14"),
        Return(),
    ]
)
