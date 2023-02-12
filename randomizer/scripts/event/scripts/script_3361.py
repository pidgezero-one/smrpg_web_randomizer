# E3361_KEEP_EXIT_COMPLETED_DOORS_TO_BOSS_ANTECHAMBER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT,
            face_direction=SOUTHEAST,
            x=2,
            y=42,
            z=10,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASShiftSoutheastPixels(3),
            ],
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJmpIfBitSet(
                    MAGIKOOPA_SAVE_ANIMATION_DONE,
                    ["EVENT_3361_action_queue_async_3_SUBSCRIPT_set_solidity_bits_19"],
                ),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(64),
                ASResetProperties(),
                ASPause(32),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(24),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(64),
                ASStartLoopNTimes(7),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASEndLoop(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(48),
                ASFaceNorthwest(),
                ASResetProperties(),
                ASSetSolidityBits(
                    cant_pass_walls=True,
                    identifier="EVENT_3361_action_queue_async_3_SUBSCRIPT_set_solidity_bits_19",
                ),
                ASFloatingOn(),
                ASJumpToHeight(height=0, silent=True),
                ASPlaySound(sound=SO019_LONG_FALL, channel=4),
                ASPause(
                    1, identifier="EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_23"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3361_action_queue_async_3_SUBSCRIPT_pause_23"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
                ASSetBit(MAGIKOOPA_SAVE_ANIMATION_DONE),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        Return(),
    ]
)
