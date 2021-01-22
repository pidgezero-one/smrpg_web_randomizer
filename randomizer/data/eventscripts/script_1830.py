from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1830_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1830_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1830_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1830_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1830_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 775]
    },
    {
        "identifier": 'EVENT_1830_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 775]
    },
    {
        "identifier": 'EVENT_1830_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1830_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1830_pause_6']
    },
    {
        "identifier": 'EVENT_1830_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1830_reset_coords_9',
        "command": 'reset_coords',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1830_store_coin_amount_7000_10',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1830_stop_embedded_action_script_23']
    },
    {
        "identifier": 'EVENT_1830_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1830_set_short_13',
        "command": 'set_short',
        "args": [0x700c, 0x0005]
    },
    {
        "identifier": 'EVENT_1830_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'EVENT_1830_store_coin_amount_7000_15',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1830_pause_20']
    },
    {
        "identifier": 'EVENT_1830_create_packet_at_object_coords_jmp_if_null_17',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._017_SMALL_COIN_NOT_MOVING, AreaObjects.MARIO, 'EVENT_1830_pause_20']
    },
    {
        "identifier": 'EVENT_1830_set_18',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1830_dec_coins_19',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1830_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1830_add_short_21',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'EVENT_1830_end_loop_22',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1830_stop_embedded_action_script_23',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1830_dec_24',
        "command": 'dec',
        "args": [0x70cb]
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_byte_25',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70cb, 0, 'EVENT_1864_slow_down_music_6']
    },
    {
        "identifier": 'EVENT_1830_fade_out_to_black_async_duration_26',
        "command": 'fade_out_to_black_async_duration',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1830_set_7000_to_current_level_27',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_28',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 321, 'EVENT_1830_enter_area_44']
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_29',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 457, 'EVENT_1830_enter_area_52']
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_30',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 455, 'EVENT_1830_set_short_mem_35']
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 322, 'EVENT_1830_enter_area_54']
    },
    {
        "identifier": 'EVENT_1830_jmp_if_var_equals_short_32',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 458, 'EVENT_1830_enter_area_62']
    },
    {
        "identifier": 'EVENT_1830_enter_area_33',
        "command": 'enter_area',
        "args": [Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, RadialDirections.NORTHEAST, 22, 123, 0, []]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_34',
        "command": 'jmp_to_event',
        "args": [1836]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1830_set_7000_to_object_coord_37',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000]
    },
    {
        "identifier": 'EVENT_1830_set_7000_to_object_coord_39',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x7030, 0x7000]
    },
    {
        "identifier": 'EVENT_1830_enter_area_41',
        "command": 'enter_area',
        "args": [Rooms._455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS, RadialDirections.NORTHEAST, 6, 47, 1, []]
    },
    {
        "identifier": 'EVENT_1830_set_bit_42',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_43',
        "command": 'jmp_to_event',
        "args": [1825]
    },
    {
        "identifier": 'EVENT_1830_enter_area_44',
        "command": 'enter_area',
        "args": [Rooms._321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, RadialDirections.NORTHEAST, 4, 62, 7, []]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1830_pause_70']
    },
    {
        "identifier": 'EVENT_1830_set_bit_46',
        "command": 'set_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_47',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1830_run_event_as_subroutine_48',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1830_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_bit_50',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_51',
        "command": 'jmp_to_event',
        "args": [1824]
    },
    {
        "identifier": 'EVENT_1830_enter_area_52',
        "command": 'enter_area',
        "args": [Rooms._457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, RadialDirections.NORTHEAST, 2, 57, 0, []]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_53',
        "command": 'jmp_to_event',
        "args": [1835]
    },
    {
        "identifier": 'EVENT_1830_enter_area_54',
        "command": 'enter_area',
        "args": [Rooms._322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, RadialDirections.NORTHEAST, 8, 115, 2, []]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_subroutine_55',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1830_pause_70']
    },
    {
        "identifier": 'EVENT_1830_set_bit_56',
        "command": 'set_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_57',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1830_run_event_as_subroutine_58',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1830_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_bit_60',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_61',
        "command": 'jmp_to_event',
        "args": [1826]
    },
    {
        "identifier": 'EVENT_1830_enter_area_62',
        "command": 'enter_area',
        "args": [Rooms._458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, RadialDirections.NORTHEAST, 10, 122, 5, []]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_subroutine_63',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1830_pause_70']
    },
    {
        "identifier": 'EVENT_1830_set_bit_64',
        "command": 'set_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_65',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1830_run_event_as_subroutine_66',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1830_clear_bit_67',
        "command": 'clear_bit',
        "args": [0x7094, 5]
    },
    {
        "identifier": 'EVENT_1830_set_bit_68',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1830_jmp_to_event_69',
        "command": 'jmp_to_event',
        "args": [1827]
    },
    {
        "identifier": 'EVENT_1830_pause_70',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1830_freeze_all_npcs_until_return_71',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1830_jmp_if_bit_set_72',
        "command": 'jmp_if_bit_set',
        "args": [0x7095, 4, 'EVENT_1830_pause_75']
    },
    {
        "identifier": 'EVENT_1830_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1830_action_queue_async_73_SUBSCRIPT_swap_short_mem_0',
                "command": 'swap_short_mem',
                "args": [0x7038, 0x7016]
            },
            {
                "identifier": 'EVENT_1830_action_queue_async_73_SUBSCRIPT_swap_short_mem_1',
                "command": 'swap_short_mem',
                "args": [0x703a, 0x7018]
            },
            {
                "identifier": 'EVENT_1830_action_queue_async_73_SUBSCRIPT_swap_short_mem_2',
                "command": 'swap_short_mem',
                "args": [0x703c, 0x701a]
            },
            {
                "identifier": 'EVENT_1830_action_queue_async_73_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x99]
            }
        ]
    },
    {
        "identifier": 'EVENT_1830_jmp_74',
        "command": 'jmp',
        "args": ['EVENT_1830_ret_81']
    },
    {
        "identifier": 'EVENT_1830_pause_75',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_1830_set_short_mem_77',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1830_set_7016_to_object_xyz_78',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1830_add_short_79',
        "command": 'add_short',
        "args": [0x701a, 0x0140]
    },
    {
        "identifier": 'EVENT_1830_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1830_action_queue_async_80_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1830_action_queue_async_80_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1830_action_queue_async_80_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1830_action_queue_async_80_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_1830_ret_81',
        "command": 'ret'
    }
]
