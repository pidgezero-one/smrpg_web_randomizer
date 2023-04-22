# pylint: disable=C0301

"""E3481_MIDAS_RIVER_TUNNEL_WARP_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1),
        Pause(4, identifier="EVENT_3481_pause_1"),
        Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_Y, pixel=True),
        Mem7000AndConst(0xFF00),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4352, ["EVENT_3481_set_7000_to_object_coord_9"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 7680, ["EVENT_3481_set_7000_to_object_coord_16"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 10496, ["EVENT_3481_set_7000_to_object_coord_31"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 14848, ["EVENT_3481_set_7000_to_object_coord_38"]
        ),
        Jmp(["EVENT_3481_pause_1"]),
        Set7000ToObjectCoord(
            target_npc=NPC_1,
            coord=COORD_X,
            pixel=True,
            identifier="EVENT_3481_set_7000_to_object_coord_9",
        ),
        Mem7000AndConst(0xFF00),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4352, ["EVENT_3481_pause_1"]),
        JmpToSubroutine(["EVENT_3481_pause_action_script_45"]),
        Db(bytearray(b"\xfdG")),
        EnterArea(
            room_id=R070_MIDAS_RIVER_1ST_TUNNEL,
            face_direction=SOUTHEAST,
            x=4,
            y=24,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        Set7000ToObjectCoord(
            target_npc=NPC_1,
            coord=COORD_X,
            pixel=True,
            identifier="EVENT_3481_set_7000_to_object_coord_16",
        ),
        Mem7000AndConst(0xFF00),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3072, ["EVENT_3481_clear_bit_21"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4608, ["EVENT_3481_set_bit_26"]),
        Jmp(["EVENT_3481_pause_1"]),
        ClearBit(MIDAS_RIVER_TUNNEL_2_DIRECTION, identifier="EVENT_3481_clear_bit_21"),
        JmpToSubroutine(["EVENT_3481_pause_action_script_45"]),
        Db(bytearray(b"\xfdG")),
        EnterArea(
            room_id=R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT,
            face_direction=SOUTHEAST,
            x=3,
            y=57,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetBit(MIDAS_RIVER_TUNNEL_2_DIRECTION, identifier="EVENT_3481_set_bit_26"),
        JmpToSubroutine(["EVENT_3481_pause_action_script_45"]),
        Db(bytearray(b"\xfdG")),
        EnterArea(
            room_id=R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT,
            face_direction=SOUTHEAST,
            x=16,
            y=67,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        Set7000ToObjectCoord(
            target_npc=NPC_1,
            coord=COORD_X,
            pixel=True,
            identifier="EVENT_3481_set_7000_to_object_coord_31",
        ),
        Mem7000AndConst(0xFF00),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 2048, ["EVENT_3481_pause_1"]),
        JmpToSubroutine(["EVENT_3481_pause_action_script_45"]),
        Db(bytearray(b"\xfdG")),
        EnterArea(
            room_id=R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT,
            face_direction=SOUTHEAST,
            x=28,
            y=25,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        Set7000ToObjectCoord(
            target_npc=NPC_1,
            coord=COORD_X,
            pixel=True,
            identifier="EVENT_3481_set_7000_to_object_coord_38",
        ),
        Mem7000AndConst(0xFF00),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 6912, ["EVENT_3481_pause_1"]),
        JmpToSubroutine(["EVENT_3481_pause_action_script_45"]),
        Db(bytearray(b"\xfdG")),
        EnterArea(
            room_id=R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT,
            face_direction=SOUTHEAST,
            x=10,
            y=97,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_3481_pause_action_script_45"),
        PlaySound(sound=SO032_UNDERGROUND_WARP, channel=6),
        StartAsyncEmbeddedActionScript(
            target=NPC_1,
            prefix=0xF1,
            subscript=[
                ASStartLoopNTimes(9),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
            ],
        ),
        PixelateLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=8, duration=196
        ),
        EnableControls([]),
        Return(),
    ]
)
