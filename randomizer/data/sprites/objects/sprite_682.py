# SPR0682_CULEX_STATUE

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL795_CULEX_STATUE
sprite = CompleteSprite(
    animation=AnimationPack(420, length=63, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x08\x02\x1a\x02\xf9\x01\x9e`\xd9\x04w\x009\x04_@\x00\x00\x00\x00\x00\x08!I\x00.\x00\x18\x00\x06\x00\x00'),
                            bytearray(b'\x10\x009\x01\xd7\x01\x82\x00\x11\x10)(\xff8m\x00((DD((}}\xfe\xaa\xd6\x92\x00\x00\xd6\x82'),
                            bytearray(b'\x00\x80\x00\x00\xff\x80\xc1\x1e\x0b\xf0\xee\x00<@\xd0\x00\x00\x00\x00\x00\x00\x00\x0c20\xcc\x008\x00\xc0\x00`'),
                            bytearray(b'/bJ\xc7M\xc7.d\x1f\x01_LcX*\x19\x00\x00\x02\x02\x04\x00\x05\x00\x81\x00\xa4\x00\x05\x01\x07\x03'),
                            bytearray(b'\x01\x10\xab9\xd6\x93p\xc1z\xfe\xe0\xf0\xcf\\\xab)\xeeDD\x00\xba\x00\x0c\x03II\xcf\x03\x05!D\x11'),
                            bytearray(b't\x04p\xc4uE`Bp\x02\\D\x880\xa82\x80\xa0\x08\x00\x80\x00\xc0\x00\x80\x00\xe2\x80D\x00@\x00'),
                            bytearray(b'~_^A?0\x0e\x04\x0f\x00\x0e\x00\x00\x00\x00\x00\x9f\x03\x03\x03\x01\x01\x03\x07\x04\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf4\xb0\xff\xc6\x8e\x8en$\xefD\xc7 \xff@f\x00\x03\x8b\xc7\x81\xff}\xdb\xffx|||$d\x00\x00'),
                            bytearray(b'\xf8\xf2\xfc\x043 f\xc0\xfc@\xb8 \xc8@\xf0\x00P\x80\x82\x80\xc0\xe0\xc0\xc0\x80\xc0`@p\x10\x00\x00'),
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
            ]
        )
    ),
    palette_id=SPAL795_CULEX_STATUE,
    palette_offset=0,
    unknown_num=0
)
