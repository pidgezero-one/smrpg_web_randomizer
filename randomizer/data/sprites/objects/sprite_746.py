# SPR0746_WATER_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL049_WATER_FIRE_CRYSTAL_3D
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x18\x00\x10 \x10(\x08\\<\xc0$\xc0\x18\xc2\x1e\x18\x18\x10\x18\x10\x1c\x08\x144 <"\x04"\x02 '),
                            None,
                            bytearray(b'\x03\x00\x03\x00\x07\x00\x07\x00\x05\x06\x01\x00\x03\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x06\x02\x00\x02\x02\x00\x02\x01'),
                            bytearray(b'\x80|\x82^\x81\x07\xc1GB\xe3\x00BCO\x00\x00bA`A?@\x7f\x00\xbf\x80\x7f\x80?\x80\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80@\x80@\x00\xc0\x00\xc0'),
                            bytearray(b'\x02\x01\x01\x01\x01\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x03\x00\x01\x00\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\xbf\xc0\xbf\xc0\xff\x8c\x7f\x0c\'t\xb5\xb7&6\xa2\xb6\xff\x00\xff\x00\xff\x00\x7f\x80w\x88\xb7H6\xc8\xb6H"),
                            bytearray(b'@@\x00\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'24<<\x0c\x0c\x18\x1888\x00\x00\x00\x00\x00\x006H<@\x0cp\x18`8\x00\x000\x000\x000'),
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
