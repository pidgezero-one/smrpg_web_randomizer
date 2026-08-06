# SPR0227_FAN_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import (CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile)
from randomizer.data.variables.sprite_palette_names import SPAL544_WAR_FAN
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03'),
                            bytearray(b'\x00\x04\x00\x0e\x00>(T\x06r*\xd6\x1e\xe2\x1c\xa0\x02\x06\x00\x0e\x01?*~\x08|$\xf8\x00\xfc`\xdc'),
                            bytearray(b'\x00\x00\x00\x03\x00\x00\x01\x07\t\x08\x08\t\x0e\n\x0f\x01\x03\x03\x0c\x0f\x0f\x0f\x19\x1e\x14\x1f\x15\x1e693<'),
                            bytearray(b'|\x84|\x04|\x04\xbcd\xbc\xe4\xfc\x84\xfcT|\xb4\x04\xf8\x04\xf8\x00\xfc`\x9c\xe0\x18\x80xP\xa8\xb0H'),
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
    palette_id=SPAL544_WAR_FAN,
    palette_offset=0,
    unknown_num=8
)
