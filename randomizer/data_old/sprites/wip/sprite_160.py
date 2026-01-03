
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(134, length=42, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x12\x06\xf1\xfa\x02\x12\xfe\x07v\x01\x12\x00\xe1\xfa\x02\x12\x0e\xee\xfa\x02\x12\x0e\xe7\xfa\x02\x12\x07\xe3\xfa\x02\x12'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x08\xf7\xfa\x02\x12\x0b\xfd\xfa\x02\x12\x10\xf3\xfa\x02\x12\x01\x04\xfa\x02\x12\xf8\x04\xfa\x02\x12\xf8\xe2\xfa\x02\x12\xff\xdd'),
                            bytearray(b'\xfa\x02\x12\x04\x07\xfa\x02\x12\xf8\x03v\x01\x12\xf9\xe8v\x01\x12\xf9\xf3v\x01\x12\x07\xde\xfa\x02\x12\x00\xf0\xfa\x02'),
                            bytearray(b'\xf0\xf7\xe8J"@]\x00\x12\xfe\xfbv\x01\x12\x04\xfa}\x01"\x01\xff4\t"\xf8\x02\x06\x04\x12\xf3\xfbv'),
                            bytearray(b'\x02\x12\xfa\xee\xfa\x02\x12\x02\xe5\xfa\x02\x12\r\xee\xfa\x02\x12\r\xe7\xfa\x02\x12\x07\xe1\xfa\x02\x12\x13\xe9\xfa\x02\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfc}\x01\xa0\xe6\xebC;\xc0\xf3\xf43\x08"\xfa\x00\x8d\x01"\xfc\xfe(\x01\x12\xf4\xffv\x01\x12\xfc\xf4\xfa'),
                            bytearray(b'\x14\xeb\xfa\x02\x12\x06\xf9\xfa\x02\x12\n\xfe\xfa\x02\x12\x10\xf5\xfa\x02\x12\x05\x08\xfa\x02\x12\xfa\x01v\x01\x12\xf8\xeb'),
                            bytearray(b'v\x01\x12\xf8\xf3v\x01\x12\x06\xde\xfa\x02\x12\xfe\xee\xfa\x02\xf0\xf5\xe6J"@]\x00\x12\xfe\xfa\xfa\x02\x12\x00'),
                            bytearray(b'\xfa\x02\x12\x00\xf2\xfa\x02\xf0\xf7\xeaJ"@]\x00\x12\xfe\xf7\xfa\x02\x12\xfc\xfc}\x01"\xfe\x00\x1b\n"\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=116),
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
    palette_id=543,
    palette_offset=0,
    unknown_num=0
)
