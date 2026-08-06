# SPR0581_STANDALONE_THRAX


from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL024_PIRANHA_PLANT
sprite = CompleteSprite(
    animation=AnimationPack(86, length=464, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=6144,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x12\x0f\x11\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x0098'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000p'),
                            bytearray(b'ax\x06uo}\x01b\x0f\x08\x0e\x02\x02\x06\x14\x1c\x1b\x1c\x1b\x10\x13\x10n1(\x17\x01\x0f\x00\x06\x02\x1e'),
                            bytearray(b'\x00\x80\x80\x00\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x04\x07\x00\x00\x00\x00'),
                            bytearray(b'  \x18\x183\x11l\r\x1c\x0c\x96\x86\xc6\xe66\x06Xx$<.?\xf2\xff\xf3\xffy\xff\x19\x8f\t\x07'),
                            bytearray(b'*:\nz0\xf04\xf4x\xf0\xe8\xe0\xde\xd6\xb4\x88\x06>\x06~\x0c\xfc\x0c\xfc\x08\xf8\x98\xf8\xf8\xf0\xf2\xc0'),
                            None,
                            None,
                            bytearray(b'\x16\x0e\n\n\x0f\x0e\x1f\x1f13 \x10\x00\x00\x00\x00\x01\x07\x05\x03\x01\x00\x00\x00\x0f\x01p\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03#\x9f\xf1\xe3\x90\xf9\x00\x9c\x80\x00\x02\x01\x01\x00\x00\xff\xc3\xdf\x9f\x0f\x0f\x07\x03\xe3\x81\x05\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x80\x80\xc0\xc0\xc0@\xe0 `\x00\xa0\x80@@\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
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
    palette_id=SPAL024_PIRANHA_PLANT,
    palette_offset=0,
    unknown_num=8
)
