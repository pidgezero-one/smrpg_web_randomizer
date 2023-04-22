# pylint: disable=C0301

"""E0615_MARRYMORE_LAMP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7042_3, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_256_ret_0"]),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7042_5, ["EVENT_615_run_dialog_49"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=16, silent=True),
                ASPlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
            ],
            identifier="EVENT_615_action_queue_async_5",
        ),
        PaletteSet(palette_set=89, row=7),
        Pause(60),
        FadeOutMusicToVolume(duration=2, volume=0),
        CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
        Pause(10),
        PlaySound(sound=SO054_GOODNIGHT, channel=6),
        Pause(50),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=30,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                )
            ],
        ),
        Pause(60),
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
        PauseScriptUntilEffectDone(),
        SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
        EnterArea(
            room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=SOUTH, x=8, y=13, z=1
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0
        ),
        RestoreAllHP(),
        RestoreAllFP(),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASSetSpriteSequence(index=13, is_sequence=True, looping=True)],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        Pause(80),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(46),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(23),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(60),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        StopSound(),
        Pause(30),
        FadeOutMusicToVolume(duration=2, volume=96),
        CircleMaskShrinkToObject(target=MARIO, width=255, speed=3, static=True),
        PauseScriptUntilEffectDone(),
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO047_SNOOZE, channel=6),
        Pause(60),
        StopSound(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASSetSpriteSequence(index=14, is_sequence=True, looping=True)],
        ),
        RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
        ApplyTileModToLevel(
            use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0
        ),
        PauseActionScript(MARIO),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASJumpToHeight(108),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_615_action_queue_async_45_SUBSCRIPT_pause_3"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_615_action_queue_async_45_SUBSCRIPT_pause_3"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP, identifier="EVENT_615_clear_bit_46"),
        SetBit(TEMP_7042_5),
        Return(),
        RunDialog(
            dialog_id=DI0990_STAY_LONGER_IN_SUITE_INTRO,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_615_run_dialog_49",
        ),
        RunDialog(
            dialog_id=DI0991_STAY_LONGER_IN_SUITE_PROMPT,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBSelected(["EVENT_615_clear_bit_46"]),
        SetBit(TEMP_7042_6),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_615_set_bit_58"]),
        Inc(TEMP_70AC),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Jmp(["EVENT_615_action_queue_async_5"]),
        SetBit(MARRYMORE_UNKNOWN_709F_6, identifier="EVENT_615_set_bit_58"),
        SetVarToConst(TEMP_70AC, 199),
        Jmp(["EVENT_615_action_queue_async_5"]),
    ]
)
