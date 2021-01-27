from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3376_speed_up_music_to_normal_0',
        "command": 'speed_up_music_to_normal'
    },
    {
        "identifier": 'EVENT_3376_set_7000_to_70A0_short_mem_1',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e7]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_2',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3376_jmp_if_7000_all_bits_clear_5']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_5',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[3], 'EVENT_3376_set_7000_to_70A0_short_mem_8']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_set_7000_to_70A0_short_mem_8',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e8]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_9',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3376_jmp_if_7000_all_bits_clear_12']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_12',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[3], 'EVENT_3376_set_7000_to_70A0_short_mem_15']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 3, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_set_7000_to_70A0_short_mem_15',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70e9]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_16',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3376_jmp_if_7000_all_bits_clear_19']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 4, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_18',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 4, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_all_bits_clear_19',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[3], 'EVENT_3376_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_3376_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 5, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3376_apply_solidity_mod_21',
        "command": 'apply_solidity_mod',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, 5, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x707f, 0, 'EVENT_3356_clear_bit_5']
    },
    {
        "identifier": 'EVENT_3376_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3376_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3376_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3376_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3376_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3376_run_event_as_subroutine_28',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3376_ret_29',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_run_event_as_subroutine_30',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3376_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_async_31_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3376_action_queue_async_31_SUBSCRIPT_walk_1_step_east_1',
                "command": 'walk_1_step_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_run_dialog_32',
        "command": 'run_dialog',
        "args": [1944, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_dialog_option_b_33',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3376_action_queue_async_54']
    },
    {
        "identifier": 'EVENT_3376_run_dialog_34',
        "command": 'run_dialog',
        "args": [1945, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_enter_area_35',
        "command": 'enter_area',
        "args": [Rooms._321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, RadialDirections.NORTHEAST, 4, 58, 5, []]
    },
    {
        "identifier": 'EVENT_3376_remove_from_current_level_36',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3376_fade_in_from_black_sync_37',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3376_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_sync_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3376_action_queue_sync_38_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_run_dialog_39',
        "command": 'run_dialog',
        "args": [1946, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_enter_area_40',
        "command": 'enter_area',
        "args": [Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, RadialDirections.NORTHEAST, 2, 63, 0, []]
    },
    {
        "identifier": 'EVENT_3376_remove_from_current_level_41',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3376_fade_in_from_black_sync_42',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3376_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3376_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_run_dialog_44',
        "command": 'run_dialog',
        "args": [1947, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_enter_area_45',
        "command": 'enter_area',
        "args": [Rooms._464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, RadialDirections.NORTHEAST, 3, 106, 0, []]
    },
    {
        "identifier": 'EVENT_3376_remove_from_current_level_46',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3376_fade_in_from_black_sync_47',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3376_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_sync_48_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3376_action_queue_sync_48_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_run_dialog_49',
        "command": 'run_dialog',
        "args": [1948, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_enter_area_50',
        "command": 'enter_area',
        "args": [Rooms._454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, RadialDirections.NORTHEAST, 6, 33, 0, []]
    },
    {
        "identifier": 'EVENT_3376_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_sync_51_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 39]
            },
            {
                "identifier": 'EVENT_3376_action_queue_sync_51_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3376_action_queue_sync_51_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_fade_in_from_black_async_52',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3376_run_dialog_53',
        "command": 'run_dialog',
        "args": [1949, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3376_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3376_action_queue_async_54_SUBSCRIPT_walk_1_step_west_0',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3376_action_queue_async_54_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3376_ret_55',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_mem_7000_and_const_56',
        "command": 'mem_7000_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'EVENT_3376_set_7000_short_mem_to_7000_57',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3376_set_7000_to_70A0_short_mem_58',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b7]
    },
    {
        "identifier": 'EVENT_3376_mem_7000_or_var_59',
        "command": 'mem_7000_or_var',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3376_set_70A0_short_mem_to_7000_60',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70b7]
    },
    {
        "identifier": 'EVENT_3376_set_7000_to_7000_short_mem_61',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_equals_short_62',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_3376_enter_area_69']
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_equals_short_63',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_3376_enter_area_71']
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_equals_short_64',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_3376_enter_area_73']
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_equals_short_65',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_3376_enter_area_75']
    },
    {
        "identifier": 'EVENT_3376_jmp_if_7000_equals_short_66',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_3376_enter_area_77']
    },
    {
        "identifier": 'EVENT_3376_enter_area_67',
        "command": 'enter_area',
        "args": [Rooms._321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, RadialDirections.NORTHEAST, 4, 58, 5, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_68',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_enter_area_69',
        "command": 'enter_area',
        "args": [Rooms._322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, RadialDirections.NORTHEAST, 8, 115, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_70',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_enter_area_71',
        "command": 'enter_area',
        "args": [Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, RadialDirections.NORTHEAST, 2, 63, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_72',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_enter_area_73',
        "command": 'enter_area',
        "args": [Rooms._462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA, RadialDirections.NORTHEAST, 2, 63, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_74',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_enter_area_75',
        "command": 'enter_area',
        "args": [Rooms._464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, RadialDirections.NORTHEAST, 3, 106, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_76',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3376_enter_area_77',
        "command": 'enter_area',
        "args": [Rooms._467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, RadialDirections.NORTHEAST, 22, 83, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3376_ret_78',
        "command": 'ret'
    }
]
