# SPR0229_PANTS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL697_MALLOW_WALKING_DOWN_LEFT
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=11, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x1f\x18x\xa0\xe7\x87\x80\x8f\x80GX\x10\x7f\x00\x00\x00\x18\x07x\x1f\x7f\x7f8\x7f0\xbf\x18`\xff'),
                            bytearray(b'\x00\x00\xc0\xf03?\x04\xc4\xc0\x06\xcc\x03\x9c^\xe1\xec\x00\x00\x000\xc0<\xfb\xfc\xff>\xfe3\xe1C\x1d\x0e'),
                            bytearray(b'\x80\x00c\x80\xe3\xdf\x0f\x0f\x07\x00\x16\x1a\xfb\xf5\x1e\x1e\x9f\x7f\xe0\xff\xa0\xbf\x10\xff\x07\xf8\x1e\xe5\xff\xeb\x1e\x1e'),
                            bytearray(b'1\xc1\x1e\x1aH\xb6s\xeb\xf7\xe7\xfe\xfe\x80\x80\x00\x00\xf0\xcf\x1d\xe5\xc2\xc2\x9b\x9d\xe7\xf9\xfe\xfe\x80\x80\x00\x00'),
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
    palette_id=SPAL697_MALLOW_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=8
)
