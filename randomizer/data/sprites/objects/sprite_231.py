# SPR0231_DRESS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL659_TOADSTOOL_SLAP_ATTACK
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\n\x1d\x02\x01\x07\x07\x08\x18\x03?\x00?@\x7f\x00\x7f\x1f&\x07\x1e\x07\x08\x18\x07?\x00?@\x7f\x00\x7f\x80'),
                            bytearray(b'\x90\xf0\x10\x00`\x00\xf0\x00\x98\xf0\x04\xf4\x06\xf2\x06\xf2\xf0\x00\x10\xe0`\x80\xf0\x00\xf8\x00\xf4\x0c\xf6\n\xf6\n'),
                            bytearray(b'\x00\x7fb\x7f{\x7f==<<\x9c\x9crp\x0f\x0f\x7f\x80\x7f\x80\x7f\x80=\xc2<\xc3\x9c\xe3r}\x0f\x0f'),
                            bytearray(b'\x07\xf3\x07\xf3\x07\xe3\xc7\xc1\x87\x81\x0e\x02\x1c\x0c\xf0\xf0\xf7\x0b\xf7\x0b\xe7\x1b\xc79\x87y\x0e\xf2\x1c\xec\xf0\xf0'),
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
    palette_id=SPAL659_TOADSTOOL_SLAP_ATTACK,
    palette_offset=0,
    unknown_num=8
)
