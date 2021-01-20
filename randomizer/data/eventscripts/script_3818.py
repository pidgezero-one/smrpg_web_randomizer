from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3818_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 192, 'EVENT_3818_enable_controls_until_return_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 137, 'EVENT_3818_jmp_if_bit_set_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 10, 'EVENT_3818_jmp_if_bit_clear_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 8, 'EVENT_3818_enter_area_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_enter_area_6',
        "command": 'enter_area',
        "args": [Rooms._203_MUSHROOM_WAY_AREA_01, RadialDirections.SOUTHEAST, 3, 28, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7052, 6, 'EVENT_3818_enter_area_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._205_MUSHROOM_WAY_AREA_03, RadialDirections.SOUTHWEST, 28, 89, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_enable_controls_until_return_11',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_start_battle_12',
        "command": 'start_battle',
        "args": [0x00a1, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_3818_remove_from_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_reset_and_choose_game_14',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_remove_from_current_level_16',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_set_short_18',
        "command": 'set_short',
        "args": [0x700a, 0x00cf],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_to_event_19',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_3818_action_queue_sync_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7094, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x707b, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7094, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_26',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_27',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_28',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_29',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_30',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_31',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_32',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_12, Rooms._139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70de],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_short_34',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 39, 'EVENT_3818_jmp_if_bit_clear_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_var_equals_short_35',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 45, 'EVENT_3818_jmp_if_bit_clear_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_36_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_37_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_async_38_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3818_action_queue_async_38_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_disabled_39',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._137_LANDS_END_AREA_01, 'EVENT_3818_jmp_if_bit_set_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3818_action_queue_sync_40_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_set_41',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3818_run_event_as_subroutine_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [1844],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_run_event_as_subroutine_43',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_run_event_as_subroutine_44',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_clear_45',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_3818_clear_bit_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_disabled_46',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._137_LANDS_END_AREA_01, 'EVENT_3818_clear_bit_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_play_sound_47',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_49',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_bit_clear_50',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 0, 'EVENT_3818_action_queue_sync_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_enter_area_51',
        "command": 'enter_area',
        "args": [Rooms._407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS, RadialDirections.SOUTHWEST, 26, 103, 22, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_52',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._319_LANDS_END_DESERT_AREA_06],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_53',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._402_LANDS_END_DESERT_AREA_03],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_54',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._403_LANDS_END_DESERT_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_55',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._404_LANDS_END_DESERT_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_summon_to_level_56',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._318_LANDS_END_DESERT_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_set_bit_57',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_fade_in_from_black_async_58',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_59',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_stop_sound_60',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_stop_sound_61',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_stop_sound_62',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_63',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_clear_bit_64',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_65',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_1, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_66',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_0, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_jmp_if_object_trigger_enabled_67',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_2, Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_set_bit_68',
        "command": 'set_bit',
        "args": [0x7098, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_set_bit_69',
        "command": 'set_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3818_ret_70',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
