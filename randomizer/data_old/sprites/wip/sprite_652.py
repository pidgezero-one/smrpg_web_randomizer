
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(97, length=31, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04z\x012\x02\x03\x86\x012\x00\x00\x97\x01\x00\x82\xfe\x00\xeb\x00\x12\x01\xfc\xd6\x01\x12\x01\x00\xc6\x04\x82\xfe\x00'),
                            bytearray(b'"\x02\xfa\x19\x02"\x02\x00%\x01\x12\x02\xfa,\x02R\x02\x008\x01B\x02\xffX\x01"\x03\x02n\x01"\x04'),
                            bytearray(b'%\x01B\xff\x00X\x01"\xfe\x01n\x01"\xff\xffz\x012\xff\x01\x86\x012\x00\x00\x97\x01\x002\x04\x01\xeb'),
                            bytearray(b'\x01"\x05\xfdn\x01"\x05\x00z\x012\x03\x01\x86\x012\x00\x00\x97\x01\x002\x04\x01\xeb\x00R\x02\x00\xfb\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=766,
    palette_offset=0,
    unknown_num=0
)
