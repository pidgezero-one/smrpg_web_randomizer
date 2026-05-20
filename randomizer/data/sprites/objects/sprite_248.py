# SPR0248_ARCHIPELAGO


from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL018_ARCHIPELAGO
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x00\x14\x0c7\x0e\x0f>>>\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x00\x01\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00@\x00`\x00\xf4\x0c\xf6\x0e\xce>>>\x00\x00\x00\x00\xc0\x00\xe0\x00\xe0\x0c\xc0\x0e\xc0>\x00>'),
                            bytearray(b'\x14\x0c6\x0e\x0f>?<\x1c\x1c\x03\x00\x01\x00\x00\x00\x0c\x00\x0e\x00>\x00<\x00\x1c\x03\x00\x03\x00\x01\x00\x00'),
                            bytearray(b'\x14\x006\x00N\x00~\x00\xfc\x00\xe0\x00\xc0\x00\x00\x00\x0c\x0c\x0e\x0e>\xfe\x1e\xfe\x1c\xfc\x00\xe0\x00\xc0\x00\x00'),
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
    palette_id=SPAL018_ARCHIPELAGO,
    palette_offset=0,
    unknown_num=8
)
