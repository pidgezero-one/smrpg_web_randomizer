# SPR0230_OVERALLS

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL601_OVERALLS
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00zzvv7657\x10\x10\x10\x1377\x00\x00~\x7f~\x7f>?=?\x1f\x1c\x1c\x1c8?'),
                            bytearray(b'\x00\x00\xf6\x00X\x00\x0c\x0c\x18\x18\x08\x18\x0c<\x8c\xfc\x00\x00\x08\xf0$\xc0\x0c\xf0\x18\xe0\xe8\xe8\xc0\xfc\x00\xfc'),
                            bytearray(b'773311474777\x1f\x1f\x00\x008?<?>?8?8?8?\x1f\x1f\x00\x00'),
                            bytearray(b'\x0c\xfc\xfc\xfc\x88\xb8\x88\xb8\x80\xb0\xc0\xc0\x00\x00\x00\x00\x00\xfc\x00\xfc@\xf8@\xf8@\xf0@\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
    palette_id=SPAL601_OVERALLS,
    palette_offset=0,
    unknown_num=8
)
