# SPR0249_RED_SHELL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL370_RED_SHELL
sprite = CompleteSprite(
    animation=AnimationPack(213, length=176, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x00\x07\x00\x07\x00\x03\x00\x03\x00\x03\x01\x01\x00\x00\x00\x03\x00\x07\x00\x06\x04\x01\x00\x03\x00\x02\x00\x01\x01\x00'),
                            bytearray(b'\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x00\xf8\x00\xf8\x00\xf9\x00\xf0\x00\x80\x00\xe0\x00\xf0\x08\xf0\x00\xf0\x00x\x00\xf0\t\xc0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x03\x01\x02\x01\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x03\x03\x00\x03\x00'),
                            bytearray(b'\x18\x9a2>`xf\xfb\x07\xfb\x89ft\x9bd\xb8c\x04\r@\x19\x86\x98\x04\xf8\x05f\x99\x8bD\x98G'),
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
