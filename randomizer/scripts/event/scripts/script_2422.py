# pylint: disable=C0301

"""E2422_ABYSS_ROOM_BEFORE_1ST_BOSS_LOWER_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
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
        SetBit(TEMP_7043_0),
        ClearBit(DIRECTIONAL_7045_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=4, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASShiftToXYCoords(x=23, y=53),
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthPixels(2),
                ASWalkSoutheastPixels(5),
                ASFaceNorthwest(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"$\xc0\xff\x80\xfe")),
                ASDb(bytearray(b"%\x00\t\x80\xff")),
                ASPause(32),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
