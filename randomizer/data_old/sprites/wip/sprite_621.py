
from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(411, length=140, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xf3\x0f\x96B\x04\xf9\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdc\xf5$"\xfe\x05\xe9\x01\x92\xff\x04Q\x01\x00R\x02\xfd2'),
                            bytearray(b'\x80\xdf\xee\xa3\x92\x00\x01Q\x01\x00\x80\xe8\x0c\x90\x80\xec\x0fR\x80\xf1\x11\x90B\x02\xfd\xe7\x00\xc2\x00\x00\xfc\x00'),
                            bytearray(b'\x90\x80\xed\x0e\x07R\x01\xfd2\x03\xc2\x00\x00\xfc\x00\x80\xd7\xf8R\x80\xd5\xf6\x90\x80\xd7\xf3\x90\xe0\xe2\xebk\xaf'),
                            bytearray(b'\x04\x00\x01"\x00\x00\x92\x05\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x08\x81\x03"\xfa\x08\x92\x03\x00\x80\xe7\x0c\x90\x80\xeb\x10RR\x01\xff\xe3\x00\xc2\x00\x00\xfc\x00"\xff\x02/\x02'),
                            bytearray(b'\x03\x80\xea\n\x90"\x00\xfc\xe1\x04\xc2\x00\x00\xfc\x00\x80\xdd\xf3$\x92\xfd\x07Q\x01\x00\x80\x05\x05t\xd0\x05\xf5'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=97),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xf3\x0f\x96B\x04\xf9\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdc\xf5$"\xfe\x05\xe9\x01\x92\xff\x04Q\x01\x00R\x02\xfd2'),
                            bytearray(b'\xf0\xc2\xe3\x12)\x98\x9c\xf0\xc2\xd3:\xbb\x83\x1d\x00\xc0\xd4\xcf\xb2w\xf0\xcc\xdf;l0\x95\xb0\xc4\xcf\x87\x92'),
                            bytearray(b'\xb1\xd0\xe2\xdbz\x0ce\xc0\xda\xcbv\x97\xf0\xd2\xeb\xbd\t\x17\xa8\xf0\xd2\xdb\x1f\xa1\xaeu\xb0\xca\xcbH\x02j'),
                            bytearray(b'\x92\xfc\x07Q\x01\x00\xa0\x03\xf5\x9f\xa0"\x00\x00\x92\x05\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x08\x81\x03"\xfa\x08\x92\x03\x00\x80\xe7\x0c\x90\x80\xeb\x10RR\x01\xff\xe3\x00\xc2\x00\x00\xfc\x00"\xff\x02/\x02'),
                            bytearray(b'\x03\x80\xea\n\x90"\x00\xfc\xe1\x04\xc2\x00\x00\xfc\x00\x80\xdd\xf3$\x92\xfd\x07Q\x01\x00\x80\x05\x05t\xd0\x05\xf5'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=98),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xf3\x0f\x96B\x04\xf9\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdc\xf5$"\xfe\x05\xe9\x01\x92\xff\x04Q\x01\x00R\x02\xfd2'),
                            bytearray(b'\xf0\xc2\xe3\x12)\x98\x9c\xf0\xc2\xd3:\xbb\x83\x1d\x00\xc0\xd4\xcf\xb2w\xf0\xcc\xdf;l0\x95\xb0\xc4\xcf\x87\x92'),
                            bytearray(b'\xb1\xd0\xe2\xdbz\x0ce\xc0\xda\xcbv\x97\xf0\xd2\xeb\xbd\t\x17\xa8\xf0\xd2\xdb\x1f\xa1\xaeu\xb0\xca\xcbH\x02j'),
                            bytearray(b'\x92\xfc\x07Q\x01\x00\xa0\x03\xf5\x9f\xa0"\x00\x00\x92\x05\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x08\x81\x03"\xfa\x08\x92\x03\x00\x80\xe7\x0c\x90\x80\xeb\x10RR\x01\xff\xe3\x00\xc2\x00\x00\xfc\x00"\xff\x02/\x02'),
                            bytearray(b'\x03\x80\xea\n\x90"\x00\xfc\xe1\x04\xc2\x00\x00\xfc\x00\x80\xdd\xf3$\x92\xfd\x07Q\x01\x00\x80\x05\x05t\xd0\x05\xf5'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=98),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00M0'),
                            bytearray(b'\x80\xdb\xf4$\x80\xdb\xf2\x07\x80\xdf\xef\xa3\x92\x00\x02Q\x01\x00\x80\xe9\x0b\x90\x80\xed\x10\xa3\x80\xf2\x11\x96B\x03'),
                            bytearray(b'Np\xbc\xe7g\xa9\x9d\xb0\xbc\xd7\xb3|\xb4\xf0\xb4\xdfITO\xaa\x80\xe7\x0c\x90\x80\xee\x0f\x90R\x00\xfe2'),
                            bytearray(b'\xb5r\xf0\xb8\xe9\x04o\n^"\x00\x00\xda\x03R\x00\xfe2\x03\xc2\x00\x00\xfc\x00\x80\xd6\xfeR\x80\xd3\xfe\x90'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00M6\t\x00\x01"\x00\x00\x92\x05\x12\x00\x00i\x05\x12\x00\x00'),
                            bytearray(b'K\x8d\x1c\xf0\xf5\x058Z\xb6\x16\xf0\xf5\xf5\x81\xab9[\x80\xeb\n\x96\x80\xef\n$\x80\xf3\t\x07\xc2\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=93),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x80\xea\n\x90\x80\xee\x0c\xa3\x80\xf1\x0e\x96\xc2\x00\x00\xfc\x00\x80\xdd\xf2$\x92\xfe\x06Q\x01\x00R\x04\xf82'),
                            bytearray(b'*[2\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00\xa0\xfd\xf0\x9f\xa0"\x00\x00\x92\x05'),
                            bytearray(b'\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00\x80\x05\xf5\x89\xe0\x05\xfd/tQ\x12\x00\x00i\x05\xf0\xf5\xf5\x81\xab'),
                            bytearray(b'\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00\xa0\t\xfa\x9f\xa0"\x00\x00\x92\x05'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xf3\x0f\x96B\x04\xf9\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdc\xf5$"\xfe\x05\xe9\x01\x92\xff\x04Q\x01\x00R\x02\xfd2'),
                            bytearray(b'\x80\xdf\xee\xa3\x92\x00\x01Q\x01\x00\x80\xe8\x0c\x90\x80\xec\x0fR\x80\xf1\x11\x90B\x02\xfd\xe7\x00\xc2\x00\x00\xfc\x00'),
                            bytearray(b'\x90\x80\xed\x0e\x07R\x01\xfd2\x03\xc2\x00\x00\xfc\x00\x80\xd7\xf8R\x80\xd5\xf6\x90\x80\xd7\xf3\x90\xe0\xe2\xebk\xaf'),
                            bytearray(b'\x04\x00\x01"\x00\x00\x92\x05\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x08\x81\x03"\xfa\x08\x92\x03\x00\x80\xe7\x0c\x90\x80\xeb\x10RR\x01\xff\xe3\x00\xc2\x00\x00\xfc\x00"\xff\x02/\x02'),
                            bytearray(b'\x03\x80\xea\n\x90"\x00\xfc\xe1\x04\xc2\x00\x00\xfc\x00\x80\xdd\xf3$\x92\xfd\x07Q\x01\x00\x80\x05\x05t\xd0\x05\xf5'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=98),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfb\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdb\xf5$"\x00\x04\xa2\x01\x92\xff\x03Q\x01\x00\x80\xea\x0b\x90\x80\xef\x0f\xa3\x80'),
                            bytearray(b'\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00\x80\x12'),
                            bytearray(b'\x03\xc2\x00\x00\xfc\x00\x80\xd7\xfdR\x80\xd5\xfd\x90\x80\xd4\xf9\x90"\xfe\x05\x81\x03"\xfe\x05\x92\x03\x00\xc0\xc8\xe9'),
                            bytearray(b'\x80\xd1\xfc\x90\xc0\xd3\xd4v\x972\xf9\t\xa0\x03"\xf9\t\x81\x03"\xf9\t\x92\x03\x00"\x00\x00\xda\x03R\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=113),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xfb\xe7\x00\xc2\x00\x00\xfc\x00\x80\xdb\xf5$"\x00\x04\xa2\x01\x92\xff\x03Q\x01\x00\x80\xea\x0b\x90\x80\xef\x0f\xa3\x80'),
                            bytearray(b'\x12\x00\x00i\x05\x12\x00\x00\xa1\x052\x00\x00w\x05\xc2\x00\x00\xfc\x00\x80\xdd\xf4$\x92\xfc\x07Q\x01\x00\x80\x12'),
                            bytearray(b'\x03\x80\xea\x0b\x90\x80\xef\x0e\xa3\x80\xf1\x0e\x96\xc2\x00\x00\xfc\x00\x80\xde\xf2$\x92\xfe\x05Q\x01\x00R\x03\xfa2'),
                            bytearray(b'\xfe2\x03\xc2\x00\x00\xfc\x00\x80\xd7\xfeR\x80\xd3\xfd\x90\x80\xd2\xfc\x90\xc0\xd4\xd3v\x972\xfa\x08\xa0\x03"\xfa'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
            ]
        )
    ),
    palette_id=477,
    palette_offset=0,
    unknown_num=0
)
