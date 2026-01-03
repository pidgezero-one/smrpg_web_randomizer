
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(350, length=92, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x12\x0b\xf1v\x01\x12\n\xe2v\x01\x12\x15\xecv\x01\x12\x08\xffv\x01\x12\x0b\x05v\x01\x12\x12\xf9v\x01\x12'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xeev\x01\x12\x01\xf8v\x01\x12\xff\x03\xf3\x02\x12\x07\xf9\xfa\x02\x12\r\xf0\xfa\x02\x12\x08\xe2\xfa\x02\x12\x15\xe7\xfa'),
                            bytearray(b'\x12\x15\xe8\xfa\x02\x12\n\xfd\xfa\x02\x12\x0c\x04\xfa\x02\xa0\xe4\xf0C;\x12\x13\xf7\xfa\x02\x12\x01\x07\xfa\x02\x12\xfb'),
                            bytearray(b'\x08\xfev\x01\x12\x0c\x04v\x01\x12\x13\xf9v\x01\x12\x02\x02v\x01\x12\xfc\x01v\x01\x12\xf9\xe7v\x01\x12\x02\xdf'),
                            bytearray(b'v\x01\x12\xfe\xf0v\x01\x12\xff\xfav\x01\xf0\xee\xef 6R)\x12\x08\xf5v\x01\x12\r\xf0v\x01\x12\n\xe1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x8d\x01"\x04\xfe(\x01\x12\xfb\xfav\x01\x12\xfb\xf0v\x01\x12\xfe\xf8v\x01\x12\x03\xeav\x01\x12\x04\xf3v'),
                            bytearray(b'v\x01\xf0\xfd\xf2J"@]\x12\n\xffv\x01\xa0\xe4\xefC;\x12\n\x05v\x01\xf0\xfa\x00J"@]\x12'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03v\x01\x12\xfd\x02v\x01\x12\xfa\xe6v\x01\x12\x03\xdev\x01\xf0\xf9\xe9\x06G\n4\x00\xf0\xef\xeb 6'),
                            bytearray(b'R)\xf0\xe8\x08J"@]\x12\x00\xfe}\x01\xc0\xf2\xf83\x08"\x04\x00\x8d\x01"\x06\xfe(\x01\x12\xf4\xfd'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfa\x02\x12\x00\xf0v\x01\x12\x01\xf8v\x01\x12\x00\x03\xf3\x02\x12\x08\xf8\xfa\x02\x12\x0c\xee\xfa\x02\x12\x08\xe0\xfa\x02'),
                            bytearray(b'v\x01\xf0\xfa\xec\x06G\n4\x00\x12\x00\x01v\x01\x12\x01\xff}\x01\xa0\xe6\xeeC;\xc0\xf2\xf93\x08"\x02'),
                            bytearray(b'\x02\x12\x0b\xfd\xfa\x02\x12\x0b\x04\xfa\x02\xa0\xe4\xf0C;\x12\x14\xf5\xfa\x02\x12\x03\x07\xfa\x02\x12\xfc\x00\xfa\x02\x12'),
                            bytearray(b'\x04v\x01\x12\xfb\xe1\xfa\x02\x12\x03\xdc\xfa\x02\xf0\xf8\xe6J"@]\x00\x12\x06\xf6\xf3\x02\x12\x03\xfb\xf3\x02\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\xfd\xf3\x02\x12\x00\xff\xfa\x02\x12\xfe\xfe}\x01\xc0\xf1\xf83\x08"\x05\x00\x8d\x01"\x07\xfe(\x01\x12\xf6\xfe'),
                            bytearray(b'\x01\xfe\xfa\x02\x12\xfd\xfe}\x01\xc0\xf1\xf83\x08\x80\xe4\nL\xf0\xdc\xfa\x11\x038^\x12\xf4\xf8\xfa\x02\x12\xfe'),
                            bytearray(b'\x01\x12\xfe\xf9v\x01\x12\x02\xeav\x01\x12\x03\xf2v\x01\x12\n\xf0v\x01\x12\n\xe1v\x01\x12\x14\xedv\x01\x12'),
                            bytearray(b'\x02\x04v\x01\x12\xfc\x03v\x01\xf0\xe2\xeaJ"@]\xf0\xea\xe4J"@]\xf0\xfa\xe7J"@]\x00\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x8d\x01"\x04\xfe(\x01\x12\xfb\xfav\x01\x12\xfb\xf0v\x01\x12\xfe\xf8v\x01\x12\x03\xeav\x01\x12\x04\xf3v'),
                            bytearray(b'v\x01\xf0\xfd\xf2J"@]\x12\n\xffv\x01\xa0\xe4\xefC;\x12\n\x05v\x01\xf0\xfa\x00J"@]\x12'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=133),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03v\x01\x12\xfd\x02v\x01\x12\xfa\xe6v\x01\x12\x03\xdev\x01\xf0\xf9\xe9\x06G\n4\x00\xf0\xef\xeb 6'),
                            bytearray(b'R)\xf0\xe8\x08J"@]\x12\x00\xfe}\x01\xc0\xf2\xf83\x08"\x04\x00\x8d\x01"\x06\xfe(\x01\x12\xf4\xfd'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=133),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfa\x02\x12\x00\xf0v\x01\x12\x01\xf8v\x01\x12\x00\x03\xf3\x02\x12\x08\xf8\xfa\x02\x12\x0c\xee\xfa\x02\x12\x08\xe0\xfa\x02'),
                            bytearray(b'v\x01\xf0\xfa\xec\x06G\n4\x00\x12\x00\x01v\x01\x12\x01\xff}\x01\xa0\xe6\xeeC;\xc0\xf2\xf93\x08"\x02'),
                            bytearray(b'\x02\x12\x0b\xfd\xfa\x02\x12\x0b\x04\xfa\x02\xa0\xe4\xf0C;\x12\x14\xf5\xfa\x02\x12\x03\x07\xfa\x02\x12\xfc\x00\xfa\x02\x12'),
                            bytearray(b'\x04v\x01\x12\xfb\xe1\xfa\x02\x12\x03\xdc\xfa\x02\xf0\xf8\xe6J"@]\x00\x12\x06\xf6\xf3\x02\x12\x03\xfb\xf3\x02\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\xfd\xf3\x02\x12\x00\xff\xfa\x02\x12\xfe\xfe}\x01\xc0\xf1\xf83\x08"\x05\x00\x8d\x01"\x07\xfe(\x01\x12\xf6\xfe'),
                            bytearray(b'\x01\xfe\xfa\x02\x12\xfd\xfe}\x01\xc0\xf1\xf83\x08\x80\xe4\nL\xf0\xdc\xfa\x11\x038^\x12\xf4\xf8\xfa\x02\x12\xfe'),
                            bytearray(b'\x01\x12\xfe\xf9v\x01\x12\x02\xeav\x01\x12\x03\xf2v\x01\x12\n\xf0v\x01\x12\n\xe1v\x01\x12\x14\xedv\x01\x12'),
                            bytearray(b'\x02\x04v\x01\x12\xfc\x03v\x01\xf0\xe2\xeaJ"@]\xf0\xea\xe4J"@]\xf0\xfa\xe7J"@]\x00\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x8d\x01"\x04\xfe(\x01\x12\xfb\xfav\x01\x12\xfb\xf0v\x01\x12\xfe\xf8v\x01\x12\x03\xeav\x01\x12\x04\xf3v'),
                            bytearray(b'v\x01\xf0\xfd\xf2J"@]\x12\n\xffv\x01\xa0\xe4\xefC;\x12\n\x05v\x01\xf0\xfa\x00J"@]\x12'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=134),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x03v\x01\x12\xfd\x02v\x01\x12\xfa\xe6v\x01\x12\x03\xdev\x01\xf0\xf9\xe9\x06G\n4\x00\xf0\xef\xeb 6'),
                            bytearray(b'R)\xf0\xe8\x08J"@]\x12\x00\xfe}\x01\xc0\xf2\xf83\x08"\x04\x00\x8d\x01"\x06\xfe(\x01\x12\xf4\xfd'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=134),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfa\x02\x12\x00\xf0v\x01\x12\x01\xf8v\x01\x12\x00\x03\xf3\x02\x12\x08\xf8\xfa\x02\x12\x0c\xee\xfa\x02\x12\x08\xe0\xfa\x02'),
                            bytearray(b'v\x01\xf0\xfa\xec\x06G\n4\x00\x12\x00\x01v\x01\x12\x01\xff}\x01\xa0\xe6\xeeC;\xc0\xf2\xf93\x08"\x02'),
                            bytearray(b'\x02\x12\x0b\xfd\xfa\x02\x12\x0b\x04\xfa\x02\xa0\xe4\xf0C;\x12\x14\xf5\xfa\x02\x12\x03\x07\xfa\x02\x12\xfc\x00\xfa\x02\x12'),
                            bytearray(b'\x04v\x01\x12\xfb\xe1\xfa\x02\x12\x03\xdc\xfa\x02\xf0\xf8\xe6J"@]\x00\x12\x06\xf6\xf3\x02\x12\x03\xfb\xf3\x02\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\xfd\xf3\x02\x12\x00\xff\xfa\x02\x12\xfe\xfe}\x01\xc0\xf1\xf83\x08"\x05\x00\x8d\x01"\x07\xfe(\x01\x12\xf6\xfe'),
                            bytearray(b'\x01\xfe\xfa\x02\x12\xfd\xfe}\x01\xc0\xf1\xf83\x08\x80\xe4\nL\xf0\xdc\xfa\x11\x038^\x12\xf4\xf8\xfa\x02\x12\xfe'),
                            bytearray(b'\x01\x12\xfe\xf9v\x01\x12\x02\xeav\x01\x12\x03\xf2v\x01\x12\n\xf0v\x01\x12\n\xe1v\x01\x12\x14\xedv\x01\x12'),
                            bytearray(b'\x02\x04v\x01\x12\xfc\x03v\x01\xf0\xe2\xeaJ"@]\xf0\xea\xe4J"@]\xf0\xfa\xe7J"@]\x00\x12'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=118),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                    ]
                ),
            ]
        )
    ),
    palette_id=368,
    palette_offset=0,
    unknown_num=0
)
