# SPR0249_RED_SHELL

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL370_RED_SHELL
sprite = CompleteSprite(
    animation=AnimationPack(213, length=176, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x00\x02\r\x07\x18\x00?\x11\x04\x0es,W\x00\x03\x00\x0f\x0f\x10\x1f ?@\x04{q\x08s\x08'),
                            bytearray(b'\x00\x00\x00\xf0 \x08\x90\n\x80q\x0eq\x88@\x98\x06\x00\xe0\xf0\x08\x0e\xd0\t\xf4p\x8ep\x8eG\xbe\x07\xfe'),
                            bytearray(b'\x10o\x08\xff\x00>\xe0\xfd`npw8;\x0f\x08\x8f`\x07\xf0\xc6\x19\x03\xebq,(W\x1c \x07\x0f'),
                            bytearray(b'\x16\x07\x06\x0f\x0c}8\xfb\x01\x1f\x02\xfe\x0c\xec\xf00N\xfe~\xfe\xfe\xfd\xfc\xfa\xe0\x0f\x00\xfa\x10\xcc\xc0\xf0'),
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
            ]
        )
    ),
    palette_id=SPAL370_RED_SHELL,
    palette_offset=0,
    unknown_num=0
)
