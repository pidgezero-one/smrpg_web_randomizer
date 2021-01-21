from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3362_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x703e, 0x703c]
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 21, 'EVENT_3362_set_short_mem_18']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 22, 'EVENT_3362_set_short_mem_22']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 23, 'EVENT_3362_set_short_mem_26']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_5',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 24, 'EVENT_3362_set_short_mem_30']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_6',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 25, 'EVENT_3362_set_short_mem_34']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 26, 'EVENT_3362_set_short_mem_38']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 27, 'EVENT_3362_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_9',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 28, 'EVENT_3362_set_short_mem_46']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 29, 'EVENT_3362_set_short_mem_50']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 30, 'EVENT_3362_set_short_mem_54']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 31, 'EVENT_3362_set_short_mem_58']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 32, 'EVENT_3362_set_short_mem_62']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 33, 'EVENT_3362_set_short_mem_66']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_15',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 34, 'EVENT_3362_set_short_mem_70']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_16',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 35, 'EVENT_3362_set_short_mem_74']
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_equals_byte_17',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 36, 'EVENT_3362_set_short_mem_78']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_19',
        "command": 'mem_7000_xor_const',
        "args": [0x0013]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_23',
        "command": 'mem_7000_xor_const',
        "args": [0x0027]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_27',
        "command": 'mem_7000_xor_const',
        "args": [0x004e]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_30',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_31',
        "command": 'mem_7000_xor_const',
        "args": [0x008c]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_35',
        "command": 'mem_7000_xor_const',
        "args": [0x0131]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_39',
        "command": 'mem_7000_xor_const',
        "args": [0x0272]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_43',
        "command": 'mem_7000_xor_const',
        "args": [0x04e4]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_47',
        "command": 'mem_7000_xor_const',
        "args": [0x08c8]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_51',
        "command": 'mem_7000_xor_const',
        "args": [0x1310]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_52',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_54',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_55',
        "command": 'mem_7000_xor_const',
        "args": [0x2720]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_59',
        "command": 'mem_7000_xor_const',
        "args": [0x4e40]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_60',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_61',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_62',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_63',
        "command": 'mem_7000_xor_const',
        "args": [0x8c80]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_64',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_66',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_67',
        "command": 'mem_7000_xor_const',
        "args": [0x3100]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_68',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_70',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_71',
        "command": 'mem_7000_xor_const',
        "args": [0x7200]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_72',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_74',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_75',
        "command": 'mem_7000_xor_const',
        "args": [0xe400]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_77',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_78',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_3362_mem_7000_xor_const_79',
        "command": 'mem_7000_xor_const',
        "args": [0xc800]
    },
    {
        "identifier": 'EVENT_3362_set_short_mem_80',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_3362_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_3362_set_82']
    },
    {
        "identifier": 'EVENT_3362_set_82',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_3362_start_loop_n_times_83',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3362_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 281]
    },
    {
        "identifier": 'EVENT_3362_add_85',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_3362_end_loop_86',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3362_action_queue_async_87',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3362_action_queue_async_87_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_87_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_87_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_87_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3362_jmp_if_var_not_equals_short_88',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703e, 65535, 'EVENT_3362_ret_102']
    },
    {
        "identifier": 'EVENT_3362_pause_89',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3362_action_queue_async_90',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_90_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3362_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3362_set_action_script_sync_92',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3362_play_sound_93',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3362_pause_94',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3362_play_music_default_volume_95',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY]
    },
    {
        "identifier": 'EVENT_3362_run_dialog_96',
        "command": 'run_dialog',
        "args": [1911, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3362_set_bit_97',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3362_play_sound_98',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3362_apply_tile_mod_99',
        "command": 'apply_tile_mod',
        "args": [Rooms._465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3362_apply_solidity_mod_100',
        "command": 'apply_solidity_mod',
        "args": [Rooms._465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3362_action_queue_async_101',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3362_action_queue_async_101_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3362_ret_102',
        "command": 'ret'
    }
]
