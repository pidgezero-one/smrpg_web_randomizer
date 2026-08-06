# SPR0238_STATIC_FROG_COIN_SMALL

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(163, length=121, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x01\x0e\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x00\x08\x0e\x01\x0c\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00` 0\x10\xf0\x10\xc8\x88h\x08\x00\x00\x00\x00\x00\x00 \xe0\x10\xf0\x90p\xf88X\xb8'),
                            bytearray(b'\x0f\x00\x0f\x00\x07\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x0c\x01\x06\t\x06\x01\x01\x02\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x08h\x08xX0\x10` \x00\x00\x00\x00\x00\x00X\xb8X\xb8\x18\xb8\x10\xf0 \xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=2,
    unknown_num=0
)
