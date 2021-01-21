from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 5, 'EVENT_2068_run_dialog_97']
    },
    {
        "identifier": 'EVENT_2068_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_1_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [5, 16]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_2_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 4, 'EVENT_2068_pause_41']
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 3, 'EVENT_2068_jmp_40']
    },
    {
        "identifier": 'EVENT_2068_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2068_pause_41']
    },
    {
        "identifier": 'EVENT_2068_run_dialog_6',
        "command": 'run_dialog',
        "args": [3049, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2068_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2068_pause_41']
    },
    {
        "identifier": 'EVENT_2068_pause_41',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2068_freeze_camera_42',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2068_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [53]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_43_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [53]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_44_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 4, 'EVENT_2068_start_battle_51']
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 3, 'EVENT_2068_start_battle_49']
    },
    {
        "identifier": 'EVENT_2068_start_battle_47',
        "command": 'start_battle',
        "args": [0x00b2, 46]
    },
    {
        "identifier": 'EVENT_2068_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_2068_restore_all_hp_53']
    },
    {
        "identifier": 'EVENT_2068_start_battle_49',
        "command": 'start_battle',
        "args": [0x00bb, 46]
    },
    {
        "identifier": 'EVENT_2068_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_2068_restore_all_hp_53']
    },
    {
        "identifier": 'EVENT_2068_start_battle_51',
        "command": 'start_battle',
        "args": [0x00bc, 46]
    },
    {
        "identifier": 'EVENT_2068_jmp_52',
        "command": 'jmp',
        "args": ['EVENT_2068_restore_all_hp_53']
    },
    {
        "identifier": 'EVENT_2068_restore_all_hp_53',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2068_restore_all_fp_54',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2068_pause_55',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_stop_music_56',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_2068_fade_out_music_to_volume_57',
        "command": 'fade_out_music_to_volume',
        "args": [0, 100]
    },
    {
        "identifier": 'EVENT_2068_play_music_default_volume_58',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN]
    },
    {
        "identifier": 'EVENT_2068_pause_59',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_fade_in_from_black_async_60',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2068_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_61_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_62_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_unfreeze_camera_63',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2068_pause_64',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_65',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_2068_run_dialog_95']
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_66',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_2068_run_dialog_91']
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 4, 'EVENT_2068_pause_75']
    },
    {
        "identifier": 'EVENT_2068_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 3, 'EVENT_2068_set_bit_72']
    },
    {
        "identifier": 'EVENT_2068_set_bit_69',
        "command": 'set_bit',
        "args": [0x708a, 3]
    },
    {
        "identifier": 'EVENT_2068_ret_70',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_71',
        "command": 'run_dialog',
        "args": [3052, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_set_bit_72',
        "command": 'set_bit',
        "args": [0x708a, 4]
    },
    {
        "identifier": 'EVENT_2068_ret_73',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_74',
        "command": 'run_dialog',
        "args": [3339, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_pause_75',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_pause_76',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_pause_77',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._016_OPEN_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_19',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_21',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_23',
                "command": 'play_sound',
                "args": [Sounds._025_HEEL_CLICK, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_play_sound_25',
                "command": 'play_sound',
                "args": [Sounds._016_OPEN_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_visibility_on_26',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_northeast_steps_27',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_shift_southeast_steps_28',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_walk_to_xy_coords_29',
                "command": 'walk_to_xy_coords',
                "args": [6, 16]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_stop_sound_30',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_78_SUBSCRIPT_face_southwest_31',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_pause_79',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_stop_sound_3',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_stop_sound_4',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_2068_action_queue_sync_80_SUBSCRIPT_shadow_on_5',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2068_action_queue_async_81_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_81_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 14]
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_81_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2068_action_queue_async_81_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2068_pause_82',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_pause_83',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2068_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 1006]
    },
    {
        "identifier": 'EVENT_2068_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 1006]
    },
    {
        "identifier": 'EVENT_2068_apply_tile_mod_86',
        "command": 'apply_tile_mod',
        "args": [Rooms._324_MONSTRO_TOWN_OUTSIDE, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2068_set_bit_87',
        "command": 'set_bit',
        "args": [0x708a, 5]
    },
    {
        "identifier": 'EVENT_2068_set_short_88',
        "command": 'set_short',
        "args": [0x700a, 0x00d8]
    },
    {
        "identifier": 'EVENT_2068_jmp_to_event_89',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_2068_ret_90',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_91',
        "command": 'run_dialog',
        "args": [3048, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_ret_92',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_93',
        "command": 'run_dialog',
        "args": [3045, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_ret_94',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_95',
        "command": 'run_dialog',
        "args": [3053, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2068_run_dialog_97',
        "command": 'run_dialog',
        "args": [3353, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2068_ret_98',
        "command": 'ret'
    }
]
