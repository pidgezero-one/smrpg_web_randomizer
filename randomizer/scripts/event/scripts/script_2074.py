# E2074_ENTER_MONSTRO_SEALED_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(room_id=R351_CULEXS_ROOM, face_direction=NORTH, x=29, y=45, z=0),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASShiftEastPixels(12)]),
        SetSyncActionScript(LAYER_1, A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER),
        RunEventAsSubroutine(E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False, duration=70),
        Pause(60),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASShiftSouthSteps(1),
                ASPause(30),
                ASShiftSouthSteps(1),
                ASPause(30),
                ASShiftSouthSteps(1),
                ASPause(30),
                ASShiftSouthSteps(1),
                ASPause(30),
                ASShiftSouthSteps(1),
                ASPause(30),
                ASShiftSouthSteps(1),
                ASPause(30),
            ],
        ),
        RunDialog(
            dialog_id=DI3057_MONSTRO_SUPERBOSS_PROMPT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBSelected(["EVENT_2074_action_queue_async_21"]),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2074_fade_in_from_black_async_29"]),
        ResetAndChooseGame(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASShiftNorthSteps(1),
                ASPause(30),
                ASShiftNorthSteps(1),
                ASPause(30),
                ASShiftNorthSteps(1),
                ASPause(30),
                ASShiftNorthSteps(1),
                ASPause(30),
                ASShiftNorthSteps(1),
                ASPause(30),
                ASShiftNorthSteps(1),
                ASPause(30),
            ],
            identifier="EVENT_2074_action_queue_async_21",
        ),
        JmpIfBitSet(
            MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_apply_solidity_mod_25"]
        ),
        EnterArea(
            room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4
        ),
        SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
        Jmp(["EVENT_2048_set_bit_0"]),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R324_MONSTRO_TOWN_OUTSIDE,
            mod_id=0,
            identifier="EVENT_2074_apply_solidity_mod_25",
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33
        ),
        JmpIfBitClear(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_2074_enter_area_27"]),
        JmpToEvent(E3886_END_GAME_CONTAINER_FROM_ALT_WIN_CONDITIONS),
        EnterArea(
            room_id=R324_MONSTRO_TOWN_OUTSIDE,
            face_direction=SOUTHWEST,
            x=11,
            y=63,
            z=4,
            identifier="EVENT_2074_enter_area_27",
        ),
        Jmp(["EVENT_2048_set_bit_0"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2074_fade_in_from_black_async_29"
        ),
        Pause(5),
        PlayMusicAtDefaultVolume(M58_CONVERSATION_WITH_CULEX),
        Pause(60),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Pause(15),
        SetBit(MONSTRO_MIDDLE_DOOR_COMPLETED),
        RestoreAllHP(),
        RestoreAllFP(),
        Jmp(["EVENT_2074_action_queue_async_21"]),
    ]
)
