from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1565_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_1565_action_queue_sync_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7094, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x707b, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7094, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_10',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_11',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70de],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 39, 'EVENT_1565_enter_area_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 45, 'EVENT_1565_enter_area_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1565_action_queue_sync_15_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1565_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1565_action_queue_sync_16_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1565_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1565_action_queue_async_17_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1565_action_queue_async_17_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1565_jmp_if_object_trigger_disabled_18',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._137_LANDS_END_AREA_01, 'EVENT_1565_jmp_if_bit_set_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1565_action_queue_sync_19_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1565_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1565_run_event_as_subroutine_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_run_event_as_subroutine_21',
        "command": 'run_event_as_subroutine',
        "args": [1844],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_run_event_as_subroutine_22',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_jmp_if_bit_clear_24',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1565_clear_bit_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_jmp_if_object_trigger_disabled_25',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._137_LANDS_END_AREA_01, 'EVENT_1565_clear_bit_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_enter_area_29',
        "command": 'enter_area',
        "args": [Rooms._407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS, RadialDirections.SOUTHWEST, 26, 103, 22, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_30',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_31',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_32',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_33',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_set_bit_35',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_fade_in_from_black_async_36',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1565_ret_37',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
