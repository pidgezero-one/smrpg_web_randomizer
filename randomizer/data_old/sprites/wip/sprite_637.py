
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(425, length=31, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x81\x01\xa8\x01\xcf\x01\xfc\x01,\x02W\x02\x92\x02\xc0\x02\xec\x02\x17\x03I\x03~\x03\x97\x03\xbf\x03\xea\x03\x0e'),
                            bytearray(b'\x04\x00\x00\xc0\xd9\x00\x06\x16\xa0\xd4\xf6\x0f\x14\xc0\xf5\xf8\x9f\x92\x90\xed\xe8\x95\x9a\xa0\xe5\x00\x91v\xf0\xe5\xf0\x96'),
                            bytearray(b'x\x8d\x9d\xa0\xe6\x0b\x19\x1e\xd0\xe6\xfb\x15\x1c\x18\xb0\xde\xeb\x0e\x02$p\xd6\x03\x10\t%\xb0\xd6\xf3\x17(\x1b'),
                            bytearray(b'\xf0\xce\xfb\x05\x0b\x1f\n\x80\xed\x0c\x9b\x80\xf2\r\x9b\x80\x07\x13\x84\xc0\x07\x03\x98{\xa0\xf7\x13\x8b\x99\xf0\xf7\x03'),
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
