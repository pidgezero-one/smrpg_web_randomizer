# SPR0228_GUN_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL691_GENO_ELBOW_SHOT
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x08\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x06\x01\x0fnv\x08\xf8 `\x00\x00\x00\x00\x00\x00\x06\x06\t\t~~\xf8\xf8\xe0`'),
                            bytearray(b'\x10\x1fF~pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x01\x00\x0e\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
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
    palette_id=SPAL691_GENO_ELBOW_SHOT,
    palette_offset=0,
    unknown_num=8
)
