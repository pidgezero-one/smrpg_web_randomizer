# SPR0652_MIMIC_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL766_MIMIC_STATUE
sprite = CompleteSprite(
    animation=AnimationPack(97, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x06\x03\x01\x07\x04\x0b\x08\x00\x00\x01\x01\x03\x03\x07\x07\x07\x07\t\x0c\x0c\x08\x0c\x0c'),
                            bytearray(b'\x00\x00\x00p@\xb8\x00\xf0\x00\x00\x81\x81\xe7\xe7\xff<~~\x8f\xff\x07\xff\x0f\xff\xff\xff\xff\xff\xff\xbd<\x18'),
                            bytearray(b'\x00\x00\x00\x00@@  ``\xd0\x90\xf00\xf00\x00\x00\x80\x80\xc0\xc0\xe0\xe0\xe0\xe0\x9000\x1000'),
                            bytearray(b'\t\x08\x0c\x0c\x0f\x0f\x07\x07\x07\x07\x03\x03\x00\x00\x00\x00\x0e\x0e\x0f\x0f\x0f\x0f\x07\x07\x07\x07\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xc3\x00\x03\x03\x7f\x14\xc1\xd5\x9c\xff\xff\xff\xff\xff~~<<\xff\xff\x94\xaa\xeb\xbe\x80\xff\xc1\xff\xc3\xfff~'),
                            bytearray(b'\xf0p\xf0\xf0\xf0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x00\x00pp\xf0\xf0\xf0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
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
    palette_id=SPAL766_MIMIC_STATUE,
    palette_offset=0,
    unknown_num=0
)
