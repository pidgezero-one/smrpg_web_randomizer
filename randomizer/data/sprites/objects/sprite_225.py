# SPR0225_FRYING_PAN_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL538_FRYING_PAN
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x05\x07\x07\x0e\x1c\x13\x18/p\x7f \x7f`\x7f\x03\x03\x0b\t\x1f\x17==uW//f/^_'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe8\x08\xf4\x02\xfe\x02\xfc\x00\xfe\x01\xff\xe0\xe0\xf8\xf8\x1cT\xf6\xf2\xf8\xf8=\xfd\r\xfd\x0e\xff'),
                            bytearray(b'@\x7f@\x7f\x00\x7f`_ ?0\xff\x08\xc7\x02\x81\xcf\xdf\xc7\xdf\xc7\x9f\x83\xdf@O\xc8\xcf2\xb3LL'),
                            bytearray(b'\x01\xff\x00\xfe\x00\xfe\x02\xfc\x00\xfc\x00\xf8\x00\xf0@\x80\xc6\xff#\xff\xe1\xfd\xc1\xfd\x02\xfa\x04\xf4(\xe800'),
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
    palette_id=SPAL538_FRYING_PAN,
    palette_offset=0,
    unknown_num=8
)
