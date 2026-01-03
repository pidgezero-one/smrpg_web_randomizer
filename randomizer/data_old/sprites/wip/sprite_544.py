
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(360, length=208, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03}\x01\xa0\xeb\xf3C;\x12\x03\x01\xcb\x06\x12\x08\xf1v\x01\x12\x10\xf9v\x01\x12\t\xfev\x01\x12\x12\xf2v'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x12\xff\xefv\x01\x12\x00\xfav\x01\x12\x04\xe8v\x01\xf0\xf5\xef\x06G\n4\x00\x12\x01\x00}\x01\xa0\xe9\xef'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x12\x03\xf2v\x01\x12\x0b\xefv\x01\x12\x0b\xe2v\x01\x12\x13\xeev\x01\x12\x07\xfbv\x01\x12\n\x00v\x01\x12\x11'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'C;\xc0\xf5\xf83\x08\x12\x01\x00\xcb\x06\x12\xfc\xf9v\x01\x12\xf8\xf0v\x01\x12\xfd\xf8v\x01\x12\x03\xeav\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8v\x01\x12\x03\x00v\x01\x12\xfe\xffv\x01\x12\xfb\xe8v\x01\x12\x03\xe2v\x01\xf0\xf8\xf0\x06G\n4\x00\x12'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x03}\x01\xa0\xeb\xf3C;\x12\x03\x01\xcb\x06\x12\x08\xf1v\x01\x12\x10\xf9v\x01\x12\t\xfev\x01\x12\x12\xf2v'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x12\xff\xefv\x01\x12\x00\xfav\x01\x12\x04\xe8v\x01\xf0\xf5\xef\x06G\n4\x00\x12\x01\x00}\x01\xa0\xe9\xef'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x12\x03\xf2v\x01\x12\x0b\xefv\x01\x12\x0b\xe2v\x01\x12\x13\xeev\x01\x12\x07\xfbv\x01\x12\n\x00v\x01\x12\x11'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'C;\xc0\xf5\xf83\x08\x12\x01\x00\xcb\x06\x12\xfc\xf9v\x01\x12\xf8\xf0v\x01\x12\xfd\xf8v\x01\x12\x03\xeav\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\xf8v\x01\x12\x03\x00v\x01\x12\xfe\xffv\x01\x12\xfb\xe8v\x01\x12\x03\xe2v\x01\xf0\xf8\xf0\x06G\n4\x00\x12'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x03}\x01\xa0\xeb\xf3C;\x12\x03\x01\xcb\x06\x12\x08\xf1v\x01\x12\x10\xf9v\x01\x12\t\xfev\x01\x12\x12\xf2v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x01\x12\xff\xefv\x01\x12\x00\xfav\x01\x12\x04\xe8v\x01\xf0\xf5\xef\x06G\n4\x00\x12\x01\x00}\x01\xa0\xe9\xef'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x12\x03\xf2v\x01\x12\x0b\xefv\x01\x12\x0b\xe2v\x01\x12\x13\xeev\x01\x12\x07\xfbv\x01\x12\n\x00v\x01\x12\x11'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'C;\xc0\xf5\xf83\x08\x12\x01\x00\xcb\x06\x12\xfc\xf9v\x01\x12\xf8\xf0v\x01\x12\xfd\xf8v\x01\x12\x03\xeav\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\xf8v\x01\x12\x03\x00v\x01\x12\xfe\xffv\x01\x12\xfb\xe8v\x01\x12\x03\xe2v\x01\xf0\xf8\xf0\x06G\n4\x00\x12'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x03}\x01\xa0\xeb\xf3C;\x12\x03\x01\xcb\x06\x12\x08\xf1v\x01\x12\x10\xf9v\x01\x12\t\xfev\x01\x12\x12\xf2v'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x01\x12\xff\xefv\x01\x12\x00\xfav\x01\x12\x04\xe8v\x01\xf0\xf5\xef\x06G\n4\x00\x12\x01\x00}\x01\xa0\xe9\xef'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x12\x03\xf2v\x01\x12\x0b\xefv\x01\x12\x0b\xe2v\x01\x12\x13\xeev\x01\x12\x07\xfbv\x01\x12\n\x00v\x01\x12\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'C;\xc0\xf5\xf83\x08\x12\x01\x00\xcb\x06\x12\xfc\xf9v\x01\x12\xf8\xf0v\x01\x12\xfd\xf8v\x01\x12\x03\xeav\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\xf8v\x01\x12\x03\x00v\x01\x12\xfe\xffv\x01\x12\xfb\xe8v\x01\x12\x03\xe2v\x01\xf0\xf8\xf0\x06G\n4\x00\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=17),
                        AnimationSequenceFrame(duration=4, mold_id=18),
                        AnimationSequenceFrame(duration=4, mold_id=19),
                    ]
                ),
            ]
        )
    ),
    palette_id=348,
    palette_offset=0,
    unknown_num=0
)
