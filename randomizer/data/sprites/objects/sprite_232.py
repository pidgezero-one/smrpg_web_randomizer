# SPR0232_CAPE

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL414_JONATHAN_JONES
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'@\xff\x8f\x7f?\xfa\xfa\xfa\xf4\xee\xc2\xeb\xc0\xebB\xf3\xff\xff\xff\xff\xff\xfa\xff\xfa\xff\xea\xff\xed\xff\xed\xff\xf4'),
                            bytearray(b'\x80\xc0\x00\x80@\x80\x00\xc0 \xc0\x00`\x10 \x88\xb0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0\xf0p\xf88\xfc<'),
                            bytearray(b'D\xf7e\xf5\x88p\x08p@0\x1c\x1cpp\x80\x80\xff\xf0\xff\xf2\xff\xff\xff\xff\xff\xff\xff\xff\xf0\xf0\x80\x80'),
                            bytearray(b'\x00x\x048\x18\x98\x90\x90\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xf8x\xf0p\xc0\xc0\x80\x80\x00\x00\x00\x00'),
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
    palette_id=SPAL414_JONATHAN_JONES,
    palette_offset=0,
    unknown_num=8
)
