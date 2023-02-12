# E1861_KEEP_DONKEY_ROOM_DONKEY

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7043_0),
        StopAllBackgroundEvents(),
        Pause(2),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASJumpToHeight(height=48, silent=True),
                ASShiftSoutheastSteps(2),
                ASFixedFCoordOff(),
                ASFaceNorthwest(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASSetWalkingSpeed(FAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASStartLoopNTimes(1),
                ASShiftSouthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_1861_action_queue_async_4_SUBSCRIPT_pause_11"
                ),
                ASJmpIfObjectInAir(
                    NPC_8, ["EVENT_1861_action_queue_async_4_SUBSCRIPT_pause_11"]
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASEndLoop(),
                ASShiftSouthwestSteps(2),
                ASVisibilityOff(),
            ],
        ),
        Return(),
    ]
)
