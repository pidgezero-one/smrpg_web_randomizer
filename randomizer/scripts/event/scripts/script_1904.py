# E1904_ABYSS_MACHINE_YARID_UPPER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(BATTLE_PACK_ID, 213),
        StartBattleWithPackAt700E(),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1904_fade_in_from_black_sync_15"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        FadeInFromBlack(sync=False),
        JmpIfBitSet(UNKNOWN_DIRECTIONAL_BIT_2, ["EVENT_1904_ret_14"]),
        Pause(1, identifier="EVENT_1904_pause_7"),
        CreatePacketAtObjectCoords(
            packet=P024_REGULAR_SOUND_EXPLOSION,
            object=NPC_0,
            destinations=["EVENT_1904_pause_7"],
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromSpecificLevel(
            NPC_0, R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=7, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=128, silent=True),
                ASShiftSouthSteps(3),
                ASSetAllSpeeds(NORMAL),
                ASResetProperties(),
                ASFloatingOn(),
            ],
        ),
        SetBit(UNKNOWN_DIRECTIONAL_BIT_2),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
            mod_id=1,
        ),
        Return(identifier="EVENT_1904_ret_14"),
        FadeInFromBlack(sync=True, identifier="EVENT_1904_fade_in_from_black_sync_15"),
        DisableObjectTrigger(MEM_70A8),
        ResumeActionScript(MEM_70A8),
        Return(),
    ]
)
