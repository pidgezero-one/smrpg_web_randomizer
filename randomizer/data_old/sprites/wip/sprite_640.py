
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(428, length=30, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xfe\x02\xea\x00\xf0\xd4\x05i\x10\t%\xf0\xd4\xf5\x17m(\x1b"\x00\x00;\x02B\xfa\x05\x16\x01b\x00\x00+'),
                            bytearray(b'\x80\xe9\xec\xa1\x00"\xff\x02\xca\x00B\x03\x00\xd4\x00b\xfe\x02\xea\x00\x80\xe6\x0f\x83\x80\xeb\x11\x9bB\xfa\x05\x16'),
                            bytearray(b'\x01b\x00\x00+\x01r\xf9\x03S\x01\x80\xe9\xec\xa1\x00"\xff\x02\xca\x00B\x03\x00\xd4\x00\xc0\xcc\xfdgl2'),
                            None,
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
    palette_id=8,
    palette_offset=0,
    unknown_num=0
)
