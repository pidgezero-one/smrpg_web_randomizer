# SPR0744_EARTH_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL050_WIND_EARTH_CRYSTAL_3D
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x18\x18\x10\x104\x14(\x08x\x10\xec \xc4\x1c\xc3\x0b\x00\x18\x00\x18\x00\x1c\x08\x14\x18\x04\x1c"\x00"\x16!'),
                            None,
                            bytearray(b'\x03\x00\x03\x00\x07\x00\x07\x04\x03\x00\x03\x02\x03\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x04\x02\x06\x00\x02\x02\x00\x02\x01'),
                            bytearray(b'\xe2X\xe2@\xbf\x01\xff@\xf7\x80s\x00\x7f\x03\x01\x01&A>A?@\x7f\x00\x7f\x80\x7f\x80\x7f\x80\x01\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\x00\x00\x80\x80\x00\x00\x00\x80\x00\x80\x00\x80\x80@\x80@\x00\xc0\x80@'),
                            bytearray(b'\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9f\xdb\xd7\x91\xdf\x8f\x87\x8e\x91\xe5~|\x86\xb6$0\xe4\x00\xee\x00\xfc\x00\xfd\x00\xf7\x08~\x81\xb6H4\xca'),
                            bytearray(b'\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80@\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'$48888p`  \x00\x00\x00\x00\x00\x004J8D8Dp\x0c \x18\x000\x000\x000'),
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
                )
            ]
        )
    ),
    palette_id=SPAL050_WIND_EARTH_CRYSTAL_3D,
    palette_offset=0,
    unknown_num=8
)
