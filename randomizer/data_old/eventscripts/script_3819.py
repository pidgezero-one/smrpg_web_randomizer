
from randomizer.helpers.eventtables import (
    ControllerDirections,
    RadialDirections,
    Rooms,
    Sounds,
    AreaObjects,
    NPCPackets,
    Locations,
    Shops,
    EventSequences,
    MenuTutorials,
    OverworldSequences,
    PlayableCharacters,
    EquipSlots,
    DialogDurations,
    IntroTitles,
    Colours,
    PaletteSetTypes,
    Music,
    MusicDirections,
    MusicPitch,
    Coords,
    CoordUnits,
    Tutorials,
    _0x40Flags,
    _0x60Flags,
    _0x62Flags,
    _0x63Flags,
    _0x68Flags,
    _0x6AFlags,
    _0x6BFlags,
    _0x81Flags,
    _0x84Flags)
from randomizer.helpers.objectsequencetables import (
    SequenceSpeeds,
    VramPriority,
    _0x08Flags,
    _0x0AFlags,
    _0x10Flags)
from randomizer.data import items

script = [
    {
        "identifier": "EVENT_3819_exit_star",
        "command": "run_event_as_subroutine",
        "args": [1605],
    },
    {
        "identifier": "EVENT_3819_jmp_if_bit_set_21",
        "command": "jmp_if_bit_set",
        "args": [0x7042, 3, "EVENT_3819_action_queue_sync_36"],
    },
    {
        "identifier": "EVENT_3819_clear_bit_22",
        "command": "clear_bit",
        "args": [0x7094, 2],
    },
    {
        "identifier": "EVENT_3819_clear_bit_24",
        "command": "clear_bit",
        "args": [0x7094, 1],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_25",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_5,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_26",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_6,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_27",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_7,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_28",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_8,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_29",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_9,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_30",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_10,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_31",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_11,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_32",
        "command": "summon_to_level",
        "args": [
            AreaObjects.NPC_12,
            Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
        ],
    },
    {
        "identifier": "EVENT_3819_set_7000_to_70A0_short_mem_33",
        "command": "copy_var_to_var",
        "args": [0x70DE, 0x7000]
    },
    {
        "identifier": "EVENT_3819_jmp_if_7000_equals_short_34",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 39, "EVENT_3819_jmp_if_bit_clear_50"]
    },
    {
        "identifier": "EVENT_3819_jmp_if_7000_equals_short_35",
        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 45, "EVENT_3819_jmp_if_bit_clear_50"]
    },
    {
        "identifier": "EVENT_3819_action_queue_sync_36",
        "command": "action_queue",
        "args": [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": "EVENT_3819_action_queue_sync_36_SUBSCRIPT_shift_northeast_pixels_0",
                "command": "shift_northeast_pixels",
                "args": [8],
            }
        ],
    },
    {
        "identifier": "EVENT_3819_action_queue_sync_37",
        "command": "action_queue",
        "args": [AreaObjects.NPC_0, True],
        "subscript": [
            {
                "identifier": "EVENT_3819_action_queue_sync_37_SUBSCRIPT_shift_west_pixels_0",
                "command": "shift_west_pixels",
                "args": [4],
            }
        ],
    },
    {
        "identifier": "EVENT_3819_action_queue_async_38",
        "command": "action_queue",
        "args": [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": "EVENT_3819_action_queue_async_38_SUBSCRIPT_shift_northeast_pixels_0",
                "command": "shift_northeast_pixels",
                "args": [8],
            },
            {
                "identifier": "EVENT_3819_action_queue_async_38_SUBSCRIPT_shift_z_up_pixels_1",
                "command": "shift_z_up_pixels",
                "args": [4],
            },
            {
                "identifier": "EVENT_3819_action_queue_async_38_fix_position",
                "command": "face_southwest",
            },
        ],
    },
    {
        "identifier": "EVENT_3819_jmp_if_bit_set_41",
        "command": "jmp_if_bit_set",
        "args": [0x7044, 7, "EVENT_3819_run_event_as_subroutine_43"],
    },
    {
        "identifier": "EVENT_3819_run_event_as_subroutine_42",
        "command": "run_event_as_subroutine",
        "args": [1844],
    },
    {
        "identifier": "EVENT_3819_run_event_as_subroutine_43",
        "command": "jmp_if_bit_clear",
        "args": [0x7044, 7, "EVENT_3819_jmp_to_event_13"],
    },
    {"identifier": "EVENT_3819_set_bit_0", "command": "set_bit", "args": [0x7087, 0]},
    {
        "identifier": "EVENT_3819_jmp_to_event_13",
        "command": "run_event_as_subroutine",
        "args": [15],
    },
    {
        "identifier": "EVENT_3819_jmp_if_bit_clear_7",
        "command": "jmp_if_bit_clear",
        "args": [0x7087, 0, "EVENT_3819_ret_26"],
    },
    {
        "identifier": "EVENT_3819_run_event_as_subroutine_25_",
        "command": "run_event_as_subroutine",
        "args": [3588],
    },
    {
        "identifier": "EVENT_3819_jmp_if_bit_clear_7_",
        "command": "jmp_if_bit_clear",
        "args": [0x7099, 7, "EVENT_3819_ret_26"],
    },
    {
        "identifier": "EVENT_3819_run_event_as_subroutine_25__",
        "command": "run_event_as_subroutine",
        "args": [3907],
    },
    {"identifier": "EVENT_3819_ret_26", "command": "ret"},
    {
        "identifier": "EVENT_3819_jmp_if_bit_clear_50",
        "command": "jmp_if_bit_clear",
        "args": [0x7089, 0, "EVENT_3819_action_queue_sync_36"],
    },
    {
        "identifier": "EVENT_3819_enter_area_51",
        "command": "enter_area",
        "args": [
            Rooms._407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS,
            RadialDirections.SOUTHWEST,
            26,
            103,
            22,
            [],
        ],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_52",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_53",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_54",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_55",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04],
    },
    {
        "identifier": "EVENT_3819_summon_to_level_56",
        "command": "summon_to_level",
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02],
    },
    {"identifier": "EVENT_3819_set_bit_57", "command": "set_bit", "args": [0x7044, 7]},
    {
        "identifier": "EVENT_3819_fade_in_from_black_async_58",
        "command": "fade_in_from_black_async",
    },
    {"identifier": "EVENT_3819_ret_59", "command": "ret"},
]
