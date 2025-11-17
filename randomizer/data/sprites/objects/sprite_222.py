# SPR0222_BANANA_PEEL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(175, length=118, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x01\x03\x01\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x01\x03\x01'),
                            bytearray(b'\x00\x00\x00\x80\xc0@\xa0`\xc0 \xc0 \xc0`\xe0`\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x00\xe0@\xe0@'),
                            None,
                            bytearray(b'\x03\x05\x07\x00\x87\x08\xfd\x02\xf9\x86g^\x01\x00\x00\x00\x07\x01\x07\x00\x8f\x00\xff\x00\xff\x00\x7f\x00\x01\x06\x00\x00'),
                            bytearray(b'\xf0p\xb3s\x82}\x97x\xb5{\x84d\xe0\x00\xe0\x00\xf0@\xf3\x00\xff\x00\xff\x00\xff\x00\xe4\x18\xe0\x10\xe0\x10'),
                            bytearray(b'\x00\x00\xc0\x00\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x00\x80@\x00\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x06\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x06\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00!\x00"\x01\x02 \x00\x00\x00\x00\x00\x00\x00\x00 \x00!\x00#\x10"\x11'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00'),
                            bytearray(b'\x03\x01\x02\x03 \x01\x11\t\x08\x04\x05\x04\x01\x00\r\x0c\x03\x00\x03\x00!\x00\x19\x00\x0f\x01\x06\x08\x02\x06\x0e\x02'),
                            bytearray(b'\x04"\x02&\xa8\xad\x00\x00 \x00\xc0\x00\xf0\x80\xf0\xa0&\x91&\xd9\xfdR\xff\xf8\xff\xfc\xff\xfe\xdf\xde\xaf\xac'),
                            bytearray(b' `@\xc0\x10\x90@@\x18\xf8\xc0\xc0\x00\x00D\xbc`\x00\xc0 \x90h\xc00\xf8\x04\xe0\x00\xe0\x00\xfc\x00'),
                            bytearray(b'x\x04\x00\x00\x02\x03\x03\x02\x03\x01\x04\x06\x04\x04\x00\x00\x7f\x01\x03\x1d\x03\x00\x03\x00\x03\x00\x06\x01\x04\x02\x00\x00'),
                            bytearray(b'\xf0 `\x00\x83\x83 )\x08,,\x08$\x04  \xbf\xbc\xbf\xf0\xff \x7f\x80o\x90l\x12$\x12 \x12'),
                            bytearray(b'\x00\x00``\x1c\x1c\x80\x00\xc0\x80\x00\x00\x00\x00\x00\x00\xc0x\xe0\x00\xfc\x00\xc08\xc0 \x00 \x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x06\x01\n\x05\x1b\x07\x0f\x1f\x00\x00\x00\x00\x00\x01\x00\x03\x03\x06\x04\x0b\x00\x1f\x07\x1f'),
                            bytearray(b'|8\x7f\x9d\x87{_\xbb\xbb\x7f\xf2\xf6\xe2\xe6\x80\x80\x18|\x19\xffA\xbf\x83\x7f\x1b\xffr\xf6\xe2\xe6\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x02\x01\x03\x05\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x02\x00\x06\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xd00\xe8\x18\x10\xe8\xcc4\xd0|\x00\x00\x00\x00\x00\x000\x00\xf8\x00\x18\x04L@\x8c\x82'),
                            None,
                            bytearray(b'\x06\x01\x02\x05\x03\x05\x06\x04\x04\x06\x03\x02\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x06\x01\x02\x05\x03\x00\x00\x00\x00\x00'),
                            bytearray(b'Dl$\xecd\xec\xc0\xc8\x18\x18\x00\x10 \xe0\x00\x00\x9c\x02\x1c\x02\x1c\x028\x06\x98f\x90l\xe0\x18\x00p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x08\x08\x04\x0c\t\x19r0s1V1\x00\x00\x00\x00\x08\x00\x08\x04\x19\x06\x10-b\x1de\x18'),
                            bytearray(b'\x00\x00\x00\x00\x02B@\xc4\xc4\xcc\xc5\xc5\x19\t\x1f\x0f\x00\x00\x00\x00B \x84b\x88v\x01\xfe\x19\xe6\x18\xe7'),
                            None,
                            bytearray(b'o\x10_\x00^\x11\x1f\x03\x7fG\x1e!\x18\x1f\x03\x03q\x00q`i\x12hgl\x033\x00\x1f\x00\x00\x03'),
                            bytearray(b'-\x9d\xff\x1f\xdf\x1fo\x8f\x0f\x8f~\xfe\xfc\xfc\xf0\xf0\xb8G\xfc\x03\xfc\xa3\xfc3\xb4k\x88v\xc0<\x00\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x03\x10\x0e \x18\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x07\x07\x0e\x0e88'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x1c\xe0\x06\x00\x02\x05\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\xf0\xf0\x02\x02\x05\x05'),
                            None,
                            bytearray(b'$\x18>\x00\x1b$\x1f\x02\n\x16\x08\x01\x04\x03\x00\x0088\x18\x10$"\x01\x07\x10\x1f\t\x0f\x07\x07\x00\x00'),
                            bytearray(b'\x03\x04\x06\x01\x1c\x02x\x84\x00\xf0\x00\xc0\x00\x00\x00\x00\x05\x05\x01\x01\x06\x06\x9c\x9c\xf0\xf0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
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
            ]
        )
    ),
    palette_id=523,
    palette_offset=0,
    unknown_num=0
)
