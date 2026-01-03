
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(427, length=31, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00\xd4\x00b\xff\x02\xea\x00\x80\xea\r\x9b\x80\xf0\x0e\x9bB\xff\x03\x16\x01b\x00\x00+\x01r\xfd\x02S\x01'),
                            bytearray(b'\x00"\x01\x00\xca\x00B\xff\x00\xd4\x00b\x00\x00\xea\x00\x80\xee\x0c\x9b\x80\xf3\x0c\x9bB\x01\x00\x16\x01b\x00\x00'),
                            bytearray(b'+\x01\x82\x01\x00S\x01\x00\xc0\xd8\x00\x06\x16\xa0\xd2\xf7\x0f\x14B\x01\x00\xd4\x00b\xff\x01\xea\x00"\x00\x01\x90'),
                            bytearray(b'\x01B\x00\x01\x16\x01b\x00\x00+\x01r\xff\x01S\x01\x80\xea\xeb\xa1\x00\xc0\xd9\x01\x06\x16\xa0\xd1\xf9\x0f\x14B'),
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
