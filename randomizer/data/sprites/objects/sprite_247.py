# SPR0247_HAMMER_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL349_HAMMER_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(166, length=91, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x00\x03\x04\x17\x18\x04\x03_@wr[\x08\x00\x00\x00\x00\x04\x00\x08\x00\x1f<N<v\x0cZ6'),
                            bytearray(b'@\xc0\xb8\xa8\xf8D~\x86\xbeF\xf8\x18\xe8h\xc0\xc7\x80\x00@\x00&\x00\xb2\x00A\x00\x07\x00\x17\x008\x00'),
                            bytearray(b'=]~,\x1e5\x10\r\x08\x0b\x00\x01\x00\x01\x00\x03|\x02\x7f\x00>\x00>\x00\x04\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x1e\x00>\x00\xf8\x00\xf0\x00\xc0\x00\x80\x00\x80\x00\x80\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
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
    palette_id=SPAL349_HAMMER_PACKET,
    palette_offset=0,
    unknown_num=8
)
