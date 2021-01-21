from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2416_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 0]
    },
    {
        "identifier": 'EVENT_2416_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_2416_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2416_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2416_action_queue_async_2_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2416_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 408]
    },
    {
        "identifier": 'EVENT_2416_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 6]
    },
    {
        "identifier": 'EVENT_2416_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2416_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2416_action_queue_sync_5_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2416_action_queue_sync_5_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x0f, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_2416_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2416_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2416_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2416_fade_out_to_black_async_duration_7',
        "command": 'fade_out_to_black_async_duration',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2416_stop_embedded_action_script_8',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'EVENT_2416_clear_bit_15']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2416_clear_bit_18']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'EVENT_2416_clear_bit_21']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 3, 'EVENT_2416_clear_bit_24']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'EVENT_2416_clear_bit_27']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 5, 'EVENT_2416_clear_bit_30']
    },
    {
        "identifier": 'EVENT_2416_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2416_enter_area_16',
        "command": 'enter_area',
        "args": [Rooms._226_FOREST_MAZE_AREA_02, RadialDirections.SOUTH, 16, 24, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2416_enter_area_19',
        "command": 'enter_area',
        "args": [Rooms._228_FOREST_MAZE_AREA_04, RadialDirections.SOUTH, 6, 110, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2416_enter_area_22',
        "command": 'enter_area',
        "args": [Rooms._229_FOREST_MAZE_AREA_06, RadialDirections.SOUTH, 20, 108, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2416_enter_area_25',
        "command": 'enter_area',
        "args": [Rooms._231_FOREST_MAZE_SECRET_ENTRANCE, RadialDirections.SOUTH, 19, 74, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2416_enter_area_28',
        "command": 'enter_area',
        "args": [Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, RadialDirections.SOUTH, 6, 40, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_29',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_31',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 1, 'EVENT_2416_enter_area_39']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_32',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 2, 'EVENT_2416_enter_area_41']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_33',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 3, 'EVENT_2416_enter_area_43']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_34',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 4, 'EVENT_2416_enter_area_45']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_35',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 5, 'EVENT_2416_enter_area_47']
    },
    {
        "identifier": 'EVENT_2416_jmp_if_var_equals_byte_36',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ac, 6, 'EVENT_2416_enter_area_49']
    },
    {
        "identifier": 'EVENT_2416_enter_area_37',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 4, 74, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_39',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 16, 92, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_41',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 13, 98, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_43',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 12, 86, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_44',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_45',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 9, 92, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_46',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_47',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 9, 78, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2416_enter_area_49',
        "command": 'enter_area',
        "args": [Rooms._225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, RadialDirections.SOUTH, 6, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2416_ret_50',
        "command": 'ret'
    }
]
