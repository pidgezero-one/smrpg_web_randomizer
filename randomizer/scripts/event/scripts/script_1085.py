# pylint: disable=C0301

"""E1085_MELODY_BAY_JUMP_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_1085_pause_action_script_160"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_1085_pause_action_script_163"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_1085_pause_action_script_166"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_1085_pause_action_script_169"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_1085_pause_action_script_172"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 5, ["EVENT_1085_pause_action_script_175"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 6, ["EVENT_1085_pause_action_script_178"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65535, ["EVENT_1085_pause_action_script_181"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65534, ["EVENT_1085_pause_action_script_184"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65533, ["EVENT_1085_pause_action_script_187"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65532, ["EVENT_1085_pause_action_script_190"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65531, ["EVENT_1085_pause_action_script_193"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65530, ["EVENT_1085_pause_action_script_196"]
        ),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_160"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASJumpToHeight(height=64, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\x00\xff")),
                ASPause(16),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_163"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASJumpToHeight(height=64, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x01\x80\xfe")),
                ASPause(16),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_166"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorth(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x00\xab\xfe")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_169"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorth(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$V\xffV\xfe")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_172"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\xab\xfe\x00\xfe")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_175"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASJumpToHeight(height=128, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x80\xfe@\xfe")),
                ASPause(32),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_178"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASJumpToHeight(height=128, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\xfe\x00\xfe")),
                ASPause(32),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_181"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\xab\xff")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_184"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceEast(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\xaa\x02\x00\x00")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_187"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceEast(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$U\x03U\x00")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_190"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSoutheast(),
                ASJumpToHeight(height=96, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x04\xaa\x00")),
                ASPause(24),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_193"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSoutheast(),
                ASJumpToHeight(height=128, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x80\x03\xc0\x00")),
                ASPause(32),
                ASBPL262728(),
            ]),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_196"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSoutheast(),
                ASJumpToHeight(height=128, silent=True),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x04\x00\x01")),
                ASPause(32),
                ASBPL262728(),
            ]),
        Return(),
    ]
)
