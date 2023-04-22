# pylint: disable=C0301

"""E0458_MUSHROOM_DERBY_BEGINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=7, y=65),
                ASSetWalkingSpeed(SLOW),
            ],
        ),
        ClearBit(YOSHI_UNKNOWN_7061_7),
        Db(bytearray(b"\xfdE")),
        PauseActionScript(NPC_9),
        ClearBit(TEMP_7044_5),
        EnableControls([]),
        StartSyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASTransferToXYZF(x=10, y=81, z=0, direction=EAST),
                ASFaceNortheast(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=MARIO,
            prefix=0xF1,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=10, y=81, z=0, direction=EAST),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        JmpToSubroutine(["EVENT_457_action_queue_sync_0"]),
        FadeInFromBlack(sync=True, duration=60),
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_458_jmp_to_event_13"]),
        RunBackgroundEvent(
            event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC,
            return_on_level_exit=True,
            bit_7=True,
        ),
        Return(),
        JmpToEvent(
            E3601_MUSHROOM_DERBY_YOSHI_AUTOPLAY, identifier="EVENT_458_jmp_to_event_13"
        ),
    ]
)
