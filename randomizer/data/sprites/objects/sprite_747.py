# SPR0747_STATIC_FROG_COIN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(324, length=490, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x10\x1f\x00\x1f\x00\x1f\x00?\x00\x00\x00\x07\x00\x08\x00\x03\x00\x07\x00\x1c\x00\x1c =\x00'),
                            bytearray(b'` \x08\x08\xcc\x04\xfc\x80|@"\x02\xb0\x000\x00 \xe0\x08\xf8\xc4<@<`\x9c.\xde>\xce>\xce'),
                            bytearray(b'?\x00?\x00\x1f\x00? \x1b\x00\x1b\x03\x0f\x00\x03\x02=\x00=\x00\x1f ? \x1b\x04\x18\x04\x0e\x01\x03\x04'),
                            bytearray(b'8\x000\x08\xb0\x00\xb2\x12\xa0\x00d\x84\xc8\x08  6\xce6\xce>\xce.\xce,\xdc|\x9c\xf88 \xe0'),
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
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=2,
    unknown_num=0
)
