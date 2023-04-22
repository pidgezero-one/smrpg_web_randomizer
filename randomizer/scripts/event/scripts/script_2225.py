# pylint: disable=C0301

"""E2225_KEEP_2ND_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["EVENT_2225_ret_31"]),
        JmpIfBitSet(KEEP_BOSS_2_DEFEATED, ["EVENT_2225_pause_5_"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASPause(30),
                ASFaceNorthwest(),
                ASSetSpriteSequence(index=9, is_sequence=True, looping=True),
                ASPause(10),
                ASResetProperties(),
                ASPause(10),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(10),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASShiftNorthSteps(1),
                ASSetWalkingSpeed(FASTER),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(FASTER),
                ASShiftNorthSteps(11),
            ],
        ),
        Pause(60),
        Pause(15),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=12, y=46, z=0, direction=EAST),
                ASPause(1),
                ASSetSpriteSequence(
                    index=4, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASSetPriority(3),
                ASOverwriteSolidity(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\xe0\xfd\x00\xff")),
                ASDb(bytearray(b"%\x00\r\x80\xff")),
                ASPause(44),
                ASBPL262728(),
                ASSetSpriteSequence(
                    index=23, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(5),
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(8),
                ASSetSpriteSequence(
                    index=15, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(3),
                ASSetSpriteSequence(
                    index=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        RunEventAsSubroutine(E0943_KEEP_SECOND_BOSS_ANIMATION_SUBROUTINE),
        FadeOutMusicToVolume(duration=0, volume=0),
        SetVarToConst(PRIMARY_TEMP_7000, 521),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        JmpIfBitClear(GAME_OVER, ["EVENT_2225_restore_all_hp_13"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2225_restore_all_hp_13"),
        RestoreAllFP(),
        SetBit(KEEP_BOSS_2_DEFEATED),
        SetVarToConst(PRIMARY_TEMP_7000, 521),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        JmpToEvent(E2226_KEEP_3RD_BOSS, identifier="EVENT_2225_pause_5_"),
        Return(identifier="EVENT_2225_ret_31"),
    ]
)
