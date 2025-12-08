# pylint: disable=C0301

"""E0594_MINES_BOSS_SHOVES_YOU"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        EnableControlsUntilReturn([]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_256_ret_0"]),
        StopAllBackgroundEvents(),
        UnsyncActionScript(NPC_0),
        FreezeCamera(),
        RunEventAsSubroutine(E0860_MINES_BOSS_SHOVE_SUBROUTINE),
        UnfreezeCamera(),
        Pause(30),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            face_direction=NORTHEAST,
            x=27,
            y=96,
            z=0),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(10),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=6),
                ASJumpToHeight(height=64, silent=True),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASSetWalkingSpeed(FAST),
                ASWalkNortheastSteps(2),
                ASResetProperties(),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(40),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(4),
                ASWalkSouthwestPixels(8),
                ASWalkNortheastPixels(8),
                ASWalkSouthwestPixels(6),
                ASWalkNortheastPixels(2),
                ASWalkSouthwestPixels(4),
                ASWalkNortheastPixels(4),
                ASWalkSouthwestPixels(2),
            ]),
        FadeInFromBlack(sync=True),
        PauseScriptUntilEffectDone(),
        RememberLastObject(),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
