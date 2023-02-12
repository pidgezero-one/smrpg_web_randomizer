# E3188_MOUNT_MINECART

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        ActionQueueSync(target=NPC_0, subscript=[ASSetVRAMPriority(NORMAL_PRIORITY)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASShadowOff(),
                ASFloatingOff(),
                ASTransferToObjectXY(MEM_70A8),
                ASTransferXYZFPixels(x=0, y=0, z=26, direction=NORTHEAST),
                ASFaceSouthwest(),
                ASSequencePlaybackOff(),
                ASSequenceLoopingOff(),
            ],
        ),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASPause(8),
                ASDb(bytearray(b" \x03")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASPlaySound(sound=SO048_MINECART_START, channel=4),
                ASPause(200),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(8),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
                ASDb(bytearray(b" \x07")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00\x00\x10\x00\x00\x01\x00\x00\x00\x04\x80"
                    )
                ),
                ASPause(200),
                ASSetBit(TEMP_7043_0),
                ASObjectMemoryClearBit(arg_1=0x0B, bits=[3]),
            ],
        ),
        Pause(1, identifier="EVENT_3188_pause_5"),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3188_pause_5"]),
        FadeOutToBlack(sync=False),
        Set7000ToMinecartTimer(),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
        RunMolevilleMountainSequence(),
        EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=0, y=0, z=0),
        SetBit(TEMP_7044_6),
        JmpToEvent(E1648_MINECART_ENDING),
    ]
)
