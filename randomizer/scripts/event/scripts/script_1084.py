# pylint: disable=C0301

"""E1084_MELODY_BAY_SONG_3_INPUT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_0"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_5"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_0"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_0"],
            identifier="EVENT_1084_jmp_if_bit_clear_5"),
        SetSyncActionScript(NPC_0, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=7, y=41, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_1, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 21),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_18"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_23"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_18"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_18"],
            identifier="EVENT_1084_jmp_if_bit_clear_23"),
        SetSyncActionScript(NPC_1, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7026),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=8, y=39, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_2, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 22),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_36"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_41"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_36"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_36"],
            identifier="EVENT_1084_jmp_if_bit_clear_41"),
        SetSyncActionScript(NPC_2, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7028),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=9, y=37, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_3, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 23),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_54"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_59"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_54"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_54"],
            identifier="EVENT_1084_jmp_if_bit_clear_59"),
        SetSyncActionScript(NPC_3, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702A),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=10, y=35, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_4, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 24),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_72"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_77"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_72"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_72"],
            identifier="EVENT_1084_jmp_if_bit_clear_77"),
        SetSyncActionScript(NPC_4, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702C),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=11, y=33, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_5, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 25),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_90"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_95"]),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_90"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_90"],
            identifier="EVENT_1084_jmp_if_bit_clear_95"),
        SetSyncActionScript(NPC_5, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_702E),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=12, y=31, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_6, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 26),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_108"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_113"]
        ),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_108"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_108"],
            identifier="EVENT_1084_jmp_if_bit_clear_113"),
        SetSyncActionScript(NPC_6, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7030),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastSteps(2), ASReturn()]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=13, y=29, z=0, direction=EAST),
                ASWalkSoutheastPixels(5),
                ASWalkSouthwestPixels(4),
                ASReturn(),
            ]),
        SetSyncActionScript(NPC_7, A0570_MELODY_BAY_TADPOLE_SWIMS),
        SetVarToConst(TEMP_70A9, 27),
        SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
        Set7000ToTappedButton(identifier="EVENT_1084_set_7000_to_tapped_button_126"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_1084_jmp_if_bit_clear_131"]
        ),
        Jmp(["EVENT_1084_set_7000_to_tapped_button_126"]),
        JmpIfBitClear(
            TEMP_7044_3,
            ["EVENT_1084_set_7000_to_tapped_button_126"],
            identifier="EVENT_1084_jmp_if_bit_clear_131"),
        SetSyncActionScript(NPC_7, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        PauseActionScript(MARIO),
        CopyVarToVar(from_var=Y_COORD_1, to_var=TEMP_7032),
        CopyVarToVar(from_var=Y_COORD_1, to_var=X_COORD_1),
        Pause(10),
        SetVarToConst(Y_COORD_1, 3),
        CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_7000),
        DecVarFrom7000(X_COORD_1),
        JmpToSubroutine(["EVENT_1084_jmp_if_7000_equals_short_147"]),
        Jmp(["EVENT_1074_set_bit_0"]),
        Return(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            0,
            ["EVENT_1084_pause_action_script_160"],
            identifier="EVENT_1084_jmp_if_7000_equals_short_147"),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_1084_pause_action_script_163"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_1084_pause_action_script_166"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_1084_pause_action_script_169"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_1084_pause_action_script_172"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 5, ["EVENT_1084_pause_action_script_175"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 6, ["EVENT_1084_pause_action_script_178"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65535, ["EVENT_1084_pause_action_script_181"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65534, ["EVENT_1084_pause_action_script_184"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65533, ["EVENT_1084_pause_action_script_187"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65532, ["EVENT_1084_pause_action_script_190"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65531, ["EVENT_1084_pause_action_script_193"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65530, ["EVENT_1084_pause_action_script_196"]
        ),
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_160"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_163"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_166"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_169"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_172"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_175"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_178"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_181"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_184"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_187"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_190"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_193"),
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
        PauseActionScript(MARIO, identifier="EVENT_1084_pause_action_script_196"),
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
