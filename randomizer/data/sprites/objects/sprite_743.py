# SPR0743_FIRE_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL049_WATER_FIRE_CRYSTAL_3D
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x08\x00\x10\x00\x10\x008\x00h\x00l\x08\xe0\x1c\xc8\x1e\x00\x00\x0c\x0c\x0c\x0c\x0c\x0c\x1e\x1e\x16\x1e\x03\x1f)?'),
                            None,
                            bytearray(b'\x01\x00\x03\x00\x03\x00\x07\x00\x01\x02\x01\x02\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x00\x02\x01\x03\x01\x01'),
                            bytearray(b"\xce\x1e\xe2\x1e\xff\x18\xbf\x00\xbf\x04\xff\x0c\xfe\x00\x00\x00-?!?\'?\x7f\x7f{\x7fs\x7f\x7f\x7f\xff\xff"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xe0'),
                            bytearray(b'\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'`\x1fB=n\x11L3=\x02\xbe\x00\xbe\x00>\x00\xe0\xff\xc2\xff\xee\xff\xcc\xff\xfd\xff\xff\xff\xff\xff~~'),
                            bytearray(b'\x80\x00\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xc0\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x1c\x00\x1c\x00\x1c\x00\x18\x00\x10\x00\x00\x00\x00\x00\x00\x00~~~~<<<<888800\x10\x10'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL049_WATER_FIRE_CRYSTAL_3D,
    palette_offset=0,
    unknown_num=8
)
