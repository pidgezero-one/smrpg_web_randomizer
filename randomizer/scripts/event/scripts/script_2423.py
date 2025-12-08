# pylint: disable=C0301

"""E2423_ABYSS_TRAMPOLINE_TO_1ST_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[ASSetSpriteSequence(index=0, looping=False, mirror_sprite=True)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
                ASShadowOff(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkSouthPixels(8),
            ]),
        SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
        PlaySound(sound=SO010_TRAMPOLINE, channel=6),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(4),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASClearSolidityBits(cant_pass_walls=True),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$0\x02\xe0\xfe")),
                ASDb(bytearray(b"%\x00\t\x80\xff")),
                ASPause(56),
                ASBPL262728(),
            ]),
        Pause(24),
        FreezeCamera(),
        Pause(24),
        FadeOutToBlack(sync=False, duration=16),
        StopEmbeddedActionScript(MARIO),
        JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["EVENT_2423_enter_area_14"]),
        EnterArea(
            room_id=R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
            face_direction=SOUTH,
            x=4,
            y=113,
            z=10,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN,
            face_direction=SOUTH,
            x=15,
            y=10,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_2423_enter_area_14"),
        Return(),
    ]
)
