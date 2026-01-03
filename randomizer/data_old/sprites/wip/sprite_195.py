
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(154, length=159, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x10\x02\x00\x02\x00\x04\x03\x06\x04\x02\x05\x02\x06\x02\x05\x02\x06\x02\x05\x02\x06\x02\x05\x02\x06\x02\x05\x02\x06\x02\x05'),
                            bytearray(b'\x0b\x02\x00\x00\x02\x00\x02\r\x02\x0e\x02\x0f\x04\x10\x02\x0f\x02\x0e\x02\r\x00\x02\x00\x02\n\x00\x02\x0c\x02\x0b\x00\xca'),
                            bytearray(b'\n\x02\x00\x02\n\x02\x00\x02\n\x02\x00\x02\n\x02\x00\x02\n\x02\x00\x02\n\x02\x0c\x02\x0b\x02\x0c\x02\x0b\x02\x0c\x02'),
                            bytearray(b'\x02\x06\x02\x05\x00\x02\x00\x06\x07\x02\x00\x06\x08\x02\x00\x06\x07\x02\x00\x06\x08\x04\x00\x02\t\x02\x00\x02\t\x02\x00\x02'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x81\x01\xa8\x01\xcf\x01\xfc\x01,\x02W\x02\x92\x02\xc0\x02\xec\x02\x17\x03I\x03~\x03\x97\x03\xbf\x03\xea\x03\x0e'),
                            bytearray(b'\x04\x00\x00\xc0\xd9\x00\x06\x16\xa0\xd4\xf6\x0f\x14\xc0\xf5\xf8\x9f\x92\x90\xed\xe8\x95\x9a\xa0\xe5\x00\x91v\xf0\xe5\xf0\x96'),
                            bytearray(b'x\x8d\x9d\xa0\xe6\x0b\x19\x1e\xd0\xe6\xfb\x15\x1c\x18\xb0\xde\xeb\x0e\x02$p\xd6\x03\x10\t%\xb0\xd6\xf3\x17(\x1b'),
                            bytearray(b'\xf0\xce\xfb\x05\x0b\x1f\n\x80\xed\x0c\x9b\x80\xf2\r\x9b\x80\x07\x13\x84\xc0\x07\x03\x98{\xa0\xf7\x13\x8b\x99\xf0\xf7\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'"\xf0\xea\xdf\x07!\x12\'\xb0\xe2\xcf#& \xf0\xda\xd7\x08\x1a\x11\x0c\x80\xea\xea\xa1\x00"\xff\x00\xca\x00B'),
                            bytearray(b'\x01\x00\xd4\x00b\x00\x00\xea\x00\x80\xec\x0b\x9b\x80\xf1\r\x9bB\xff\x01\x16\x01b\x00\x00+\x01\x82\xff\x00S\x01'),
                            bytearray(b'\x00\x82\x82st\xf0\xe8\xf0\x87r\x86}\x80\xfa\xef)\xc0\xfa\xdf\x03\x01\xf0\xf2\xcf*\x13\r\x1d\xa0\xea\xef\x04'),
                            bytearray(b'\x8e\x90\x93\x80\xe0\xf8\x10\xa0\x85|\xf0\xf8\x00w\x88\x9e\x97\xf0\xf8\xf0\x9c\x7fy~\xb0\xe8\x10\x81qz\xf0\xe8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x002\x1a\xfe\xeb\x00R\x17\xfd\xfb\x00\x12\x1a\xf9\xd6\x01\x12\x1a\xfd\xc6\x04\xc2\x17\xfd%\x01"\x19\xf6n\x01'),
                            bytearray(b'\xff\xff\x07\x01\x00\x00\xf0\xf8\xfd\x06\n\x05\x01\xf0\xf4\xf0\x06\n\x05\x01\x00\xc0\x00\xfd\x05\x01\xc0\xfa\xfd\x06\n\xc0'),
                            bytearray(b'\x00R\x03\x01\xfb\x00\x12\x06\xfd\xd6\x01\x12\x06\x01\xc6\x04\x82\x03\x01%\x01B\xff\x00X\x01"\x02\xffn\x01"'),
                            bytearray(b'\x00\x02\x04\x02\x03\x02\x05\x02\x00\x02\x04\x02\x03\x02\x05\x00\x02\x07\x02\x06\x02\x04\x02\x03\x02\x00\x02\x07\x02\x06\x02\x04'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04z\x012\x02\x03\x86\x012\x00\x00\x97\x01\x00\x82\xfe\x00\xeb\x00\x12\x01\xfc\xd6\x01\x12\x01\x00\xc6\x04\x82\xfe\x00'),
                            bytearray(b'"\x02\xfa\x19\x02"\x02\x00%\x01\x12\x02\xfa,\x02R\x02\x008\x01B\x02\xffX\x01"\x03\x02n\x01"\x04'),
                            bytearray(b'%\x01B\xff\x00X\x01"\xfe\x01n\x01"\xff\xffz\x012\xff\x01\x86\x012\x00\x00\x97\x01\x002\x04\x01\xeb'),
                            bytearray(b'\x01"\x05\xfdn\x01"\x05\x00z\x012\x03\x01\x86\x012\x00\x00\x97\x01\x002\x04\x01\xeb\x00R\x02\x00\xfb\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00\xd4\x00b\xff\x02\xea\x00\x80\xea\r\x9b\x80\xf0\x0e\x9bB\xff\x03\x16\x01b\x00\x00+\x01r\xfd\x02S\x01'),
                            bytearray(b'\x00"\x01\x00\xca\x00B\xff\x00\xd4\x00b\x00\x00\xea\x00\x80\xee\x0c\x9b\x80\xf3\x0c\x9bB\x01\x00\x16\x01b\x00\x00'),
                            bytearray(b'+\x01\x82\x01\x00S\x01\x00\xc0\xd8\x00\x06\x16\xa0\xd2\xf7\x0f\x14B\x01\x00\xd4\x00b\xff\x01\xea\x00"\x00\x01\x90'),
                            bytearray(b'\x01B\x00\x01\x16\x01b\x00\x00+\x01r\xff\x01S\x01\x80\xea\xeb\xa1\x00\xc0\xd9\x01\x06\x16\xa0\xd1\xf9\x0f\x14B'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x02\x02\x00\x02\x00\x02\x03\x02\x04\x04\x06\x06\x07\x00\x02\x00\x02\x04\x02\x03\x02\x05\x02\x00\x02\x04\x02\x03\x02\x05\x02'),
                            bytearray(b'\xfd\x03\x04\x80\xf9\xf6\x04\x00\xc0\xfd\xfe\x08\x0e\xc0\xf9\xf1\x08\x0e\x00\x80\x01\x02\x0b\x80\xfa\x02\x0c\xa0\xf5\xf5\x0c\x0b'),
                            bytearray(b'\x00\x80\xfd\x02\t\x80\xf9\xf5\t\x00\xf0\xf8\xfd\x07\x02\x03\r\xf0\xf4\xf0\x07\x02\x03\r\x009\x04\x0c\x00\xa6\x00\n'),
                            bytearray(b'\x04\xfez\x012\x03\xff\x86\x012\x00\x00\x97\x01\x002\r\xfe\xeb\x00R\x0b\xfd\xfb\x00\x12\x0e\xf9\xd6\x01\x12\x0e'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x03\x02\x00\x02\x07\x02\x06\x02\x04\x02\x03\x02\x00\x02\x07\x02\x06\x02\x04\x02\x03\x02\x00\x00\x02\x00\x02\x03\x02\x08\x02'),
                            bytearray(b'\x97\x01\x00\x16\x01\x0c\x00\x8f\x00\x06\t\x08\x00\x00\x00\x1a\x00\xff\xff!\x00,\x00M\x00v\x00\x00\x00\x02\x00\x02'),
                            bytearray(b'"\x15\xfbz\x012\x0c\xff\x86\x012\x00\x00\x97\x01\x002+\xfa\xeb\x00R\'\xf9\xfb\x00\x12*\xf5\xd6\x01\x12'),
                            bytearray(b'\xfc\xf0\x05\x01\xc0\xf6\xf0\x06\n\x00\xa0\xf7\x04\n\x01\xa0\xf7\xfe\x06\x05\xa0\xf3\xf7\n\x01\xa0\xf3\xf1\x06\x05\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x11 \x00\x00\x00"\x00\xff\xff+\x00\xff\xff\xff\xff\xff\xffL\x00\x8b\x00\x9c\x00\xa1\x00\x00\x00\n\x00\x10\x01\n'),
                            bytearray(b'\xfd\xc6\x04\x82\x0b\xfd%\x01B\t\xfeX\x01"\r\xfen\x01"\r\xffz\x012\x05\xff\x86\x012\x00\x00\x97'),
                            bytearray(b'*\xf9\xc6\x04\x82\'\xf9%\x01B%\xf9X\x01"\x1f\xf4n\x01"\x15\xfbz\x012\x0c\xff\x86\x012\x00\x00'),
                            bytearray(b'\x00\x02\x03\x02\x08\x02\x00\x02\x03\x02\x08\x02\x00\x02\x03\x02\x08\x00\xa3\x00\xb2\x00\xc7\x00\xdc\x00\xe5\x00\xf0\x00\xfe\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
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
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=9),
                    ]
                ),
            ]
        )
    ),
    palette_id=8,
    palette_offset=0,
    unknown_num=0
)
