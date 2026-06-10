# SPR0212_BAND_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL234_NINJA
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc1\x00\xc3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc1\xa3\xc3'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@@( \x88\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\xd8\x80\x8c\x00\x0c'),
                            bytearray(b'V\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06v\x00<\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\x00\x02\x04\x01\x02\x01\x02\x00\x02\x00\x00\x00\x00\x00\x00\x00\x06\x00\x07\x00\x03\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00'),
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
    palette_id=SPAL234_NINJA,
    palette_offset=0,
    unknown_num=8
)
