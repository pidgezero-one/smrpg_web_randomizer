# SPR0660_JINX_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL774_JINX_STATUE
sprite = CompleteSprite(
    animation=AnimationPack(385, length=130, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x03\x02\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00'),
                            bytearray(b'\x08x0\xf0@\xc0@\xc0\xc0\xc0\xa0\xe0\x10\xf0@\xe0\x00x\x00\xf0\x00\xe0@\xe0@\xc0\x00\x80\x00\x00\x10@'),
                            None,
                            bytearray(b'\x02\x01\x00\x01\x00\x07\x01\x05\x00\x01\x00\x00\x00\x03\x01\x01\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'H\x08T\xdc\xb3\xffL\xdf\x13\xdf\x9a\x9a\\\\\xc8\xf8\xb8\x80<\x02\xff\x00o\x043\x03v\x00\xfc\\\xc8\xc8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\x00\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x03\x02\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x08x0\xf0@\xc0@\xc0\xc0\xc0\xa0\xe0\x10\xf0\x00\xe0\x00x\x00\xf0\x00\xe0@\xe0@\xc0\x00\x80\x00\x00\x10\x00'),
                            None,
                            bytearray(b'\x02\x01\x01\x01\x00\x01\x01\x05\x00\x06\x00\x00\x00\x03\x01\x01\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x08\xc8\xd4\xdc\x83\xff\x01\xff\x03\xff\x9a\xda\\\\\xf0\xf08\x00<\x02\xff\x00\x7f\x00\xff\x03v\x00\xfc\\\xf0\xf0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\x00\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=1),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL774_JINX_STATUE,
    palette_offset=0,
    unknown_num=0
)
