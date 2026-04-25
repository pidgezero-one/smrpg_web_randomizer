# SPR0661_MOKURA_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL775_MOKURA_STATUE
sprite = CompleteSprite(
    animation=AnimationPack(343, length=82, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\x03\x07\x07\x03\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x04\x00\x04\x00\x04'),
                            bytearray(b'\x00\x00\x00\x00\x1e\x00\xfbg\xf1\x82\xcd\x8c\xa2>\xdcc\x00\x00\x00\x00\x00\x1e\x7f\x80\x7f\x00s\x00\xc1\x00\x80\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x80@\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\xc0 \xc0 '),
                            bytearray(b'\x03\x02\x03\x00\x02\x01\x03\x03\x07\x03\x01\x02\x00\x03\x00\x00\x03\x00\x03\x00\x02\x04\x00\x04\x00\x04\x03\x00\x01\x02\x00\x00'),
                            bytearray(b'\x9e!>\x81\x9cc\x8d\xb2\x83\x9c\xf9\xc6\x01\xe0\x00\x11\xc0\x00\xc0\x00\x80\x00A\x00c\x00?\x00\xfe\x01\x1cc'),
                            bytearray(b'`@@@\xa0@\xa0 \x00   @\xc0\x00\x00\xc0 \xc0\x00\xc0 \xe0\x00\xe0\x00\xe0\x00\xc0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL775_MOKURA_STATUE,
    palette_offset=0,
    unknown_num=0
)
