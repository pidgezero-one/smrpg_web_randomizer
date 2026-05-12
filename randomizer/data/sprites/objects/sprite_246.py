# SPR0246_STICK_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL534_STICK_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(166, length=91, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b' 0h\x1b\x00Ney\x023\x08;\x01\x03\x05\x0f \x10_\x00o\x10\x08w\x11/7\x0f\x07?\x03\x1f'),
                            bytearray(b'\x00\x00\x80\x80\x00@ \x80 @@\xe0\x80\xe0\x80\xe0\x00\x00\x80\x00\x80@`\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            bytearray(b'\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xe0\x80\xe0\x00`\x10`\x000\x080\x00\x18\x00\x0c\xe0\xe0\xe0\xe0``pp0088\x18\x18\x0c\x0c'),
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
    palette_id=SPAL534_STICK_PACKET,
    palette_offset=0,
    unknown_num=0
)
