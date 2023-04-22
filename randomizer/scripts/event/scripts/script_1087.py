# pylint: disable=C0301

"""E1087_MELODY_BAY_EXIT_WATER_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(MARIO),
        UnfreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASJumpToHeight(64),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\x00\xff")),
                ASPause(16),
                ASBPL262728(),
            ],
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_1087_pause_action_script_187_"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_1087_pause_action_script_187__"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_1087_pause_action_script_187__"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_1087_pause_action_script_187__"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65535, ["EVENT_1087_pause_action_script_187"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65534, ["EVENT_1087_pause_action_script_187"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65533, ["EVENT_1087_pause_action_script_187"]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
            identifier="EVENT_1087_pause_action_script_187",
        ),
        Jmp(["EVENT_1087_action_queue_swim__"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
            identifier="EVENT_1087_pause_action_script_187_",
        ),
        Jmp(["EVENT_1087_action_queue_swim__"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=14, sprite_offset=1, is_sequence=True, looping=True
                )
            ],
            identifier="EVENT_1087_pause_action_script_187__",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
                ASPause(10),
                ASWalkToXYCoords(x=15, y=32),
            ],
            identifier="EVENT_1087_action_queue_swim__",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASPause(10),
                ASJumpToHeight(64),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\x00\xff")),
                ASPause(16),
                ASBPL262728(),
            ],
        ),
        Return(),
    ]
)
