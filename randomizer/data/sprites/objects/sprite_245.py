# SPR0245_CHOMP_BALL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL537_CHOMP_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(166, length=91, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07\x1b\x1c)?s@>\x1e\x81\xff\xe5\xba\xd7\xa8\x07\x07\x18\x1f/0_`!@\x80\x80Y\x98\x88\x08'),
                            bytearray(b'\xe0\xe0\xb8\x18T,>\xa2\xd6z\x1dMu\xc5\t\xe9\xe0\xe0\x18\xf84\xcc\xa2F\xe4\x02\xfd\x03\xfc\x03\xd0\x07'),
                            bytearray(b'=\xf2qL\xbe\xc9\x96\xa1T_! \x11\x1f\x07\x07\xc0@\x0b\x88\xc0\x80\xb8\xc0\x1f`\x00?\x10\x1f\x07\x07'),
                            bytearray(b'\x07\xe9M_\x9f?\x0e\x9e\xde\x1e|\xfc\xf8\xf8\xe0\xe0\xd8\xc7\xb1\x0f\x85\x7fN>\xfc\x0e|\xfc\xf8\xf8\xe0\xe0'),
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
    palette_id=SPAL537_CHOMP_PACKET,
    palette_offset=0,
    unknown_num=0
)
