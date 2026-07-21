# SPR0845_CANNONBALL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone

from randomizer.data.variables.sprite_palette_names import SPAL485_CANNONBALL
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x01\x0b\x02\x1c\x17\x02\x11&7\x00\x00\x00\x00\x00\x01\x01\x06\x03\x0c\x07\x18\x03\x1c\x078'),
                            bytearray(b'\x00\x00d\x00\xcd\xc9h\xb8\x0c\xe5\xa14\x02NTN\x00\x00\x00|\xc87\xfc\x03\xdd\x02\xdc\x03\xfe\x01\xbe\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa0 \xf0  \x00h \x00\x00\x00\x00\x00\x00@\xc0\x00\xe0\x10\xf0\x10\xf0\x18\xf8'),
                            None,
                            bytearray(b'2#Y\x01J\x10\x14\\\x0bH\x1eI5\x16\x05%\x03<a~`\x7fd{p\x7fp\x7f(?:?'),
                            bytearray(b"\x8f\'^\xa6\xab\xfaKH\x1e\x01v\xc2\xfc\xb4l.\xdf\x00\xfe\x01\xfa\x05H\xb7\x00\xff\x01\xff\x03\xff\x91\xff"),
                            bytearray(b'@\x00dd\xd4@\xe8\xa4\xa8\xb4\xc0\xdc\xf0\x98\xb0\x188\xf8\x1c\xfc<\xfc\x1c\xfc\\\xfc<\xfcx\xf8\xf8\xf8'),
                            None,
                            bytearray(b'\n\x10\x15\x18\x0f\r\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x1f\x1f\x1f\x1f\x0f\x0f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'%\x04\xbdB\x93\xef#\xff\xff\xff||\x00\x00\x00\x00\xfb\xff\xff\xff\xff\xff\xff\xff\xff\xff||\x00\x00\x00\x00'),
                            bytearray(b'@\xb0 \xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL485_CANNONBALL,
    palette_offset=0,
    unknown_num=0
)
