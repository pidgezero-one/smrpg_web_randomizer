from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1119_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 1, 'EVENT_1119_jmp_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_bit_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_1119_play_music_default_volume_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_play_music_default_volume_19',
        "command": 'play_music_default_volume',
        "args": [Music._15_HERES_SOME_WEAPONS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_present_in_current_level_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_play_music_default_volume_22',
        "command": 'play_music_default_volume',
        "args": [Music._05_SEASIDE_TOWN],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_present_in_current_level_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_present_in_current_level_25',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_7, 'EVENT_1119_apply_solidity_mod_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_bit_set_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_27',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_apply_solidity_mod_28',
        "command": 'apply_solidity_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_bit_set_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_30',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_fade_in_from_black_sync_31',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 1, 'EVENT_1119_fade_in_from_black_sync_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 58, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_35_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 63, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_35_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_35_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 147],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 147],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 147],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 147],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 147],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_fade_in_from_black_async_41',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_42_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_43',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_44_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_45',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_unfreeze_camera_46',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1118_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_48_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [85]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_48_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_unsync_dialog_49',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_close_dialog_50',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_51',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_52',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_dialog_option_b_53',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1119_jmp_if_var_equals_byte_55'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_1118_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_55',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 1, 'EVENT_1119_pause_75'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_56',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 2, 'EVENT_1119_pause_96'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_57',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 3, 'EVENT_1119_pause_96'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_58_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_59_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_59_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_60',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_61_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_61_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_62_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_63',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_64',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_65',
        "command": 'pause',
        "args": [100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_66',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_69',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_70_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_71_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_set_72',
        "command": 'set',
        "args": [0x70bc, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_73',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_74',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_var_equals_byte_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_75',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_76_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_77_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_77_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_78',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_79_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_79_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_79_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_80_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_80_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_81_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_82',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_83',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_84',
        "command": 'pause',
        "args": [100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_85',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_86_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_86_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_88_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_89',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_90',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_90_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_91_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_92',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_run_dialog_93',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_run_dialog_94',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_95',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_var_equals_byte_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_96',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_97',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_97_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_98_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_98_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_99',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_102_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_102_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_102_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_102_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_103_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_103_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_103_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_103_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [18]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [18]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_105',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_106_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_106_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_107_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_107_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_107_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_108_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_108_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_108_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_109',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_109_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_109_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_109_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_110',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_111',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 3, 'EVENT_1119_run_dialog_114'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_run_dialog_112',
        "command": 'run_dialog',
        "args": [2857, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_113',
        "command": 'pause',
        "args": [100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_run_dialog_114',
        "command": 'run_dialog',
        "args": [2858, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_115',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_116',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_117_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_117_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_117_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [21]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_118_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_119_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_120_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_121',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_121_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_122',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_123',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_123_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_124',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_124_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1119_set_125',
        "command": 'set',
        "args": [0x70bc, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_pause_126',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_run_dialog_127',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1119_jmp_128',
        "command": 'jmp',
        "args": ['EVENT_1119_jmp_if_var_equals_byte_56'],
        "subscript": []
    },
]
