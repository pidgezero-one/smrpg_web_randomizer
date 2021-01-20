from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 4, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7085, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_freeze_camera_3',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_stop_all_background_events_4',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_db_5',
        "command": 'db',
        "args": [0xfd, 0x44],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_db_6',
        "command": 'db',
        "args": [0xfd, 0x45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_8',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_8_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_8_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [20, 61]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_close_dialog_9',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_10',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_11',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_11_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_11_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_11_SUBSCRIPT_object_memory_clear_bit_3',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_12',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x705e, 2, 'EVENT_3600_jmp_if_bit_set_166'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3600_action_queue_sync_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3600_action_queue_sync_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3600_action_queue_sync_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_18_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 680],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 681],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_21_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [17, 49]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_22',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_23',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_24',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_25',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_26',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_27',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_28',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_29',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_30',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_to_subroutine_31',
        "command": 'jmp_to_subroutine',
        "args": [0x8022],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_3600_action_queue_async_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ee],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_var_equals_short_34',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3600_play_sound_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_object_memory_to_36',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_remove_one_from_inventory_37',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_end_loop_38',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_39',
        "command": 'set',
        "args": [0x70ee, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_40',
        "command": 'set',
        "args": [0x70eb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_41_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_44_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_3600_run_dialog_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_46_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_46_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_run_dialog_47',
        "command": 'run_dialog',
        "args": [892, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ba],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_52',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_53',
        "command": 'set',
        "args": [0x7000, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_var_equals_short_54',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 0, 'EVENT_3600_mem_7000_shift_left_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_object_memory_to_55',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_add_56',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_end_loop_57',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_dec_short_58',
        "command": 'dec_short',
        "args": [0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_3600_jmp_if_var_equals_short_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_mem_7000_shift_left_60',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x70b8, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_62',
        "command": 'run_dialog',
        "args": [943, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_event_as_subroutine_63',
        "command": 'run_event_as_subroutine',
        "args": [3599],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_65_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [17, 49]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_jmp_to_subroutine_66',
        "command": 'jmp_to_subroutine',
        "args": [0x7fdf],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_3600_action_queue_async_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_68',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_69',
        "command": 'run_dialog',
        "args": [893, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_70',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ee],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_var_equals_short_71',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3600_jmp_79'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_mem_72',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_object_memory_to_73',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_remove_one_from_inventory_74',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_end_loop_75',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_76',
        "command": 'set',
        "args": [0x70ee, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_77',
        "command": 'set',
        "args": [0x70eb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_78_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_80_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_81',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_82',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_83',
        "command": 'run_dialog',
        "args": [894, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_84',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_85',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3600_unsync_action_script_92'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_86',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3600_unsync_action_script_98'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_87',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3600_unsync_action_script_104'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_88',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_89',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_90',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_91',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_action_script_109'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_92',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_93',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_94',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_95',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_96',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_97',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_action_script_109'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_98',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_99',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_100',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_101',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_102',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_103',
        "command": 'jmp',
        "args": ['EVENT_3600_pause_action_script_109'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_104',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_105',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_106',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_107',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_108',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_109',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_110',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_111',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_112',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_113',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_fade_out_music_to_volume_114',
        "command": 'fade_out_music_to_volume',
        "args": [3, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_115',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_music_default_volume_116',
        "command": 'play_music_default_volume',
        "args": [Music._04_YOSTER_ISLAND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_117',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_3600_action_queue_async_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_118_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_119',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_120',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_121',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_121_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_122',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_123',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_124',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_125',
        "command": 'set',
        "args": [0x70b9, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_126',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_127',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_128',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_129',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_130',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_131',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_132',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_133',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_134',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_135',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_136',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_137',
        "command": 'clear_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_138',
        "command": 'clear_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_139',
        "command": 'clear_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_140',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_to_subroutine_141',
        "command": 'jmp_to_subroutine',
        "args": [0x82fb],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_142',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 682],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_143',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 685],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_144',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 683],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_145',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 98],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_146',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_146_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_147',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_148',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_149',
        "command": 'set_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_short_150',
        "command": 'set_short',
        "args": [0x703e, 0x0007],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unfreeze_camera_151',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_152',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_3600_enable_controls_158'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_background_event_153',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enable_controls_154',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_155',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 684],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_156',
        "command": 'clear_bit',
        "args": [0x705e, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_157',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enable_controls_158',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_159',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_160',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_160_SUBSCRIPT_object_memory_clear_bit_0',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_160_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_160_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_160_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_161',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 496],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_162',
        "command": 'clear_bit',
        "args": [0x705e, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_163',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_164',
        "command": 'clear_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_165',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_jmp_if_bit_set_166',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3600_set_bit_288'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_167',
        "command": 'set',
        "args": [0x70ee, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_168',
        "command": 'set',
        "args": [0x70eb, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_169',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_169_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_170',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_170_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_171',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 680],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_172',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 681],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_173',
        "command": 'set_bit',
        "args": [0x7049, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_event_as_subroutine_174',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_175',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_176',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_176_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [21, 63, 0]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_176_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_177',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_178',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_179',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_180',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_181',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_182',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_183',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_184',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_185',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_186',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_fade_out_music_to_volume_187',
        "command": 'fade_out_music_to_volume',
        "args": [3, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_188',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_stop_music_189',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_music_default_volume_190',
        "command": 'play_music_default_volume',
        "args": [Music._04_YOSTER_ISLAND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_191',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_object_memory_clear_bit_5',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_191_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_192',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_192_SUBSCRIPT_object_memory_clear_bit_5',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_193',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_193_SUBSCRIPT_object_memory_clear_bit_5',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_remember_last_object_194',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_195',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_195_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_196',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_196_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_197',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_198',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_199',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_200',
        "command": 'run_dialog',
        "args": [912, AreaObjects.NPC_5, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_201',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_202',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_203',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_204',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_204_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_205',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_205_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_206',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_207',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_208',
        "command": 'run_dialog',
        "args": [913, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_209',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_210',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_10, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_211',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_212',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_212_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_213',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_213_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_214',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_215',
        "command": 'play_sound',
        "args": [Sounds._062_BIG_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_216',
        "command": 'run_dialog',
        "args": [2511, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_217',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_218',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_219',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_219_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_219_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_219_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_220',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_221',
        "command": 'run_dialog',
        "args": [914, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_222',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_222_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_223',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_223_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_224',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_225',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_226',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_226_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_227',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_227_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_228',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_229',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_230',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_231',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_231_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_232',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_232_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_233',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_234',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_235',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_236',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_236_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_237',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_237_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_238',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_239',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_239_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_240',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_240_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xd1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_241',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_242',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_243',
        "command": 'run_dialog',
        "args": [915, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_244',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_245',
        "command": 'play_sound',
        "args": [Sounds._062_BIG_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_246',
        "command": 'run_dialog',
        "args": [916, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_247',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_248',
        "command": 'set_bit',
        "args": [0x7085, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_249',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_250',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_250_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_250_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_250_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3600_action_queue_sync_250_SUBSCRIPT_pause_1']
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_251',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_251_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_251_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_251_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_251_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_circle_mask_static_252',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_script_until_effect_done_253',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_254',
        "command": 'set_bit',
        "args": [0x7049, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enter_area_255',
        "command": 'enter_area',
        "args": [Rooms._034_YOSTER_ISLE, RadialDirections.NORTHWEST, 20, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_256',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_257',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_258',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_258_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_258_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [21, 62, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_259',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_259_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 61, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_259_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_fade_in_from_black_sync_duration_260',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_script_until_effect_done_261',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_262',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_263',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_264',
        "command": 'run_dialog',
        "args": [917, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_265',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_266',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_267',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_268',
        "command": 'run_dialog',
        "args": [918, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_269',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_270',
        "command": 'set',
        "args": [0x70b8, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_271',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_272',
        "command": 'set',
        "args": [0x70a7, 109],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_273',
        "command": 'run_dialog',
        "args": [513, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_event_as_subroutine_274',
        "command": 'run_event_as_subroutine',
        "args": [3599],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_275',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_276',
        "command": 'run_dialog',
        "args": [919, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_277',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_278',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_279',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_280',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_280_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._063_YOSHI_TALK, 6]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_280_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_280_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_280_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_280_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_281',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 676],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_282',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_282_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_282_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_282_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_282_SUBSCRIPT_face_south_3',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_283',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_283_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_283_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_283_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_283_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_284',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_285',
        "command": 'set_bit',
        "args": [0x705e, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enable_controls_286',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_287',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_288',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_289',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_unsync_action_script_290',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_291',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_292',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_293',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_294',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_295',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_296',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_fade_out_music_to_volume_297',
        "command": 'fade_out_music_to_volume',
        "args": [3, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_298',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_stop_music_299',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_music_default_volume_300',
        "command": 'play_music_default_volume',
        "args": [Music._04_YOSTER_ISLAND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_301',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_301_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_pause_302',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_303',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_303_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_304',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_304_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_play_sound_305',
        "command": 'play_sound',
        "args": [Sounds._062_BIG_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_306',
        "command": 'run_dialog',
        "args": [911, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_circle_mask_static_307',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_script_until_effect_done_308',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_bit_309',
        "command": 'set_bit',
        "args": [0x7049, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enter_area_310',
        "command": 'enter_area',
        "args": [Rooms._034_YOSTER_ISLE, RadialDirections.NORTHWEST, 20, 61, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_311',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_action_script_312',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_313',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_313_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_313_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [21, 62, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_314',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_314_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 61, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_314_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_fade_in_from_black_sync_duration_315',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_script_until_effect_done_316',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_317',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_play_sound_318',
        "command": 'play_sound',
        "args": [Sounds._063_YOSHI_TALK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_run_dialog_319',
        "command": 'run_dialog',
        "args": [937, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_320',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_async_321',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_pause_322',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_323',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_323_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_323_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_323_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3600_action_queue_async_323_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_324',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 676],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_set_action_script_sync_325',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_enable_controls_326',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_clear_bit_327',
        "command": 'clear_bit',
        "args": [0x7099, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_ret_328',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_329',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_329_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_329_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_330',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_330_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_330_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_331',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_331_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_331_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_332',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_332_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_332_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_start_embedded_action_script_async_333',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_333_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_333_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_333_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            },
            {
                "identifier": 'EVENT_3600_start_embedded_action_script_async_333_SUBSCRIPT_object_memory_clear_bit_3',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_sync_334',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_sync_334_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3600_action_queue_sync_334_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_action_queue_async_335',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3600_action_queue_async_335_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3600_ret_336',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
