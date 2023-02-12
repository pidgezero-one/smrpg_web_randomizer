# E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PaletteSet(palette_set=33, row=7),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=3, y=9, z=3, direction=EAST),
                ASShiftSouthwestPixels(6),
                ASShiftZUpPixels(2),
                ASFaceSoutheast(),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASShadowOff(),
            ],
        ),
        SetSyncActionScript(MARIO, A0095_PLAYER_GAME_START),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASShiftSouthwestPixels(2)],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASShiftNorthPixels(4)],
        ),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
        RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
        RunEventAsSubroutine(E0181_NPC_QUEST_4_CONTAINER),
        RunEventAsSubroutine(E0182_NPC_QUEST_5_CONTAINER),
        PlayMusicAtDefaultVolume(M14_MARIOS_PAD),
        Pause(1),
        Set7000ToTappedButton(
            identifier="EVENT_2497_____set_7000_to_tapped_button_244"
        ),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_2497_____pause_action_script_249"]
        ),
        Jmp(["EVENT_2497_____set_7000_to_tapped_button_244"]),
        PauseActionScript(MARIO, identifier="EVENT_2497_____pause_action_script_249"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASFixedFCoordOff(),
                ASSequencePlaybackOn(),
                ASFaceSoutheast(),
                ASShadowOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(69),
                ASFloatingOn(),
                ASShiftSoutheastSteps(2),
                ASPause(35),
                ASPlaySound(sound=SO056_SHAKE_HEAD, channel=6),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(1),
                ASSetSpriteSequence(
                    index=8, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(30),
                ASStopSound(),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        Pause(30),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0
        ),
        Return(),
    ]
)
