# SPR0253_BERRY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone

sprite = CompleteSprite(
    animation=AnimationPack(
        118,
        length=31,
        unknown=0x0000,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=False,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=7,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x00\x02"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80@\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x03\x04\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=120,
                            y=120),
                    ]),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ])),
    palette_id=420,
    palette_offset=0,
    unknown_num=0)
