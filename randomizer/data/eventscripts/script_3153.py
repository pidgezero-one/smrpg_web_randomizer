from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 192, 'EVENT_3153_set_197']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 193, 'EVENT_3153_set_200']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 194, 'EVENT_3153_set_203']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 195, 'EVENT_3153_set_206']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 196, 'EVENT_3153_set_209']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_5',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 197, 'EVENT_3153_set_212']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_6',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 198, 'EVENT_3153_set_215']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 199, 'EVENT_3153_set_217']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 200, 'EVENT_3153_set_219']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_9',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 201, 'EVENT_3153_set_221']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 202, 'EVENT_3153_set_223']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 203, 'EVENT_3153_set_225']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 204, 'EVENT_3153_set_227']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 205, 'EVENT_3153_set_229']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 206, 'EVENT_3153_set_231']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_15',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 207, 'EVENT_3153_set_233']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_16',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 208, 'EVENT_3153_set_235']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_17',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 209, 'EVENT_3153_set_237']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_18',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 210, 'EVENT_3153_disable_trigger_241']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_19',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 150, 'EVENT_3153_set_281']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_20',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_3153_set_281']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_21',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 152, 'EVENT_3153_set_281']
    },
    {
        "identifier": 'EVENT_3153_summon_to_current_level_22',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [33]
    },
    {
        "identifier": 'EVENT_3153_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_25',
        "command": 'run_dialog',
        "args": [1177, AreaObjects.MARIO, []]
    },
    {
        "identifier": 'EVENT_3153_put_inventory_26',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_3153_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_33']
    },
    {
        "identifier": 'EVENT_3153_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_add_30',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_3153_set_short_31',
        "command": 'set_short',
        "args": [0x701c, 0x0028]
    },
    {
        "identifier": 'EVENT_3153_run_background_event_with_pause_return_on_exit_32',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1543, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_3153_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_disable_trigger_34',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_3153_disable_event_trigger_for_object_at_70A8_37',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3153_mem_7000_and_const_38',
        "command": 'mem_7000_and_const',
        "args": [0x00f0]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x70b4, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_3153_set_7010_to_object_xyz_41',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3153_add_43',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_45',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 0, 'EVENT_3153_play_sound_50']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_46',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 16, 'EVENT_3153_enable_controls_57']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_47',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 32, 'EVENT_3153_play_sound_104']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_48',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 48, 'EVENT_3153_play_sound_109']
    },
    {
        "identifier": 'EVENT_3153_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_play_sound_50',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_51',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._001_MUSHROOM, 'EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_restore_all_hp_52',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3153_restore_all_fp_53',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3153_set_short_54',
        "command": 'set_short',
        "args": [0x7020, 0x0008]
    },
    {
        "identifier": 'EVENT_3153_run_background_event_with_pause_55',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7020, [12, 13]]
    },
    {
        "identifier": 'EVENT_3153_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_enable_controls_57',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3153_play_sound_58',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_59',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._003_SUPER_STAR, 'EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_stop_music_60',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_3153_set_short_61',
        "command": 'set_short',
        "args": [0x7022, 0x0226]
    },
    {
        "identifier": 'EVENT_3153_run_background_event_with_pause_62',
        "command": 'run_background_event_with_pause',
        "args": [3076, 0x7022, [12, 13]]
    },
    {
        "identifier": 'EVENT_3153_set_bit_63',
        "command": 'set_bit',
        "args": [0x7076, 0]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_bit_clear_64',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 0, 'EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_65',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 0, 'EVENT_3153_set_74']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 1, 'EVENT_3153_set_77']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_67',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 2, 'EVENT_3153_set_80']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_68',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 3, 'EVENT_3153_set_83']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_69',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 4, 'EVENT_3153_set_86']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_70',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 5, 'EVENT_3153_set_89']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_71',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 6, 'EVENT_3153_set_92']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_72',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 7, 'EVENT_3153_set_92']
    },
    {
        "identifier": 'EVENT_3153_ret_73',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_74',
        "command": 'set',
        "args": [0x70a7, 16]
    },
    {
        "identifier": 'EVENT_3153_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_76',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_77',
        "command": 'set',
        "args": [0x70a7, 17]
    },
    {
        "identifier": 'EVENT_3153_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_79',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_80',
        "command": 'set',
        "args": [0x70a7, 18]
    },
    {
        "identifier": 'EVENT_3153_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_82',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_83',
        "command": 'set',
        "args": [0x70a7, 19]
    },
    {
        "identifier": 'EVENT_3153_jmp_84',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_85',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_86',
        "command": 'set',
        "args": [0x70a7, 20]
    },
    {
        "identifier": 'EVENT_3153_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_88',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_89',
        "command": 'set',
        "args": [0x70a7, 21]
    },
    {
        "identifier": 'EVENT_3153_jmp_90',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_91',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_92',
        "command": 'set',
        "args": [0x70a7, 23]
    },
    {
        "identifier": 'EVENT_3153_jmp_93',
        "command": 'jmp',
        "args": ['EVENT_3153_set_short_mem_95']
    },
    {
        "identifier": 'EVENT_3153_ret_94',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_95',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_3153_mem_7000_and_const_96',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3153_set_experience_packet_7000_97',
        "command": 'set_experience_packet_7000'
    },
    {
        "identifier": 'EVENT_3153_mario_glows_98',
        "command": 'mario_glows'
    },
    {
        "identifier": 'EVENT_3153_clear_bit_99',
        "command": 'clear_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_100',
        "command": 'clear_bit',
        "args": [0x7064, 4]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_101',
        "command": 'clear_bit',
        "args": [0x707c, 2]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_object_coords_jmp_if_null_102',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_3153_jmp_103']
    },
    {
        "identifier": 'EVENT_3153_jmp_103',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_play_sound_104',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_105',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 'EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_set_106',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3153_add_max_FP_7000_107',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3153_jmp_108',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_play_sound_109',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_110',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_3153_ret_112']
    },
    {
        "identifier": 'EVENT_3153_add_frog_coins_111',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3153_ret_112',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_113',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_114',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_115',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_disable_trigger_116',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_117',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 240, 'EVENT_3153_play_sound_119']
    },
    {
        "identifier": 'EVENT_3153_disable_event_trigger_for_object_at_70A8_118',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3153_play_sound_119',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_120',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_121',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_mem_7000_and_const_122',
        "command": 'mem_7000_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_123',
        "command": 'set_short_mem',
        "args": [0x70b4, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_add_124',
        "command": 'add',
        "args": [0x7000, 288]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_mem_704x_at_7000_bit_set_125',
        "command": 'jmp_if_mem_704x_at_7000_bit_set',
        "args": ['EVENT_3153_jmp_if_var_equals_byte_139']
    },
    {
        "identifier": 'EVENT_3153_set_mem_704x_at_7000_bit_126',
        "command": 'set_mem_704x_at_7000_bit'
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_127',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_3153_mem_7000_and_const_128',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_129',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3153_set_short_mem_134']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_130',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3153_set_short_mem_136']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_131',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3153_set_short_mem_138']
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_132',
        "command": 'set_short_mem',
        "args": [0x70da, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_3153_jmp_if_var_equals_byte_139']
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_134',
        "command": 'set_short_mem',
        "args": [0x70db, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_135',
        "command": 'jmp',
        "args": ['EVENT_3153_jmp_if_var_equals_byte_139']
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_136',
        "command": 'set_short_mem',
        "args": [0x70dc, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_137',
        "command": 'jmp',
        "args": ['EVENT_3153_jmp_if_var_equals_byte_139']
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_138',
        "command": 'set_short_mem',
        "args": [0x70dd, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_139',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3153_jmp_if_var_not_equals_byte_144']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_140',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3153_jmp_if_var_not_equals_byte_146']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_141',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3153_jmp_if_var_not_equals_byte_148']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_not_equals_byte_142',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70da, 1, 'EVENT_3153_set_temp_action_script_sync_151']
    },
    {
        "identifier": 'EVENT_3153_jmp_143',
        "command": 'jmp',
        "args": ['EVENT_3153_set_action_script_sync_149']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_not_equals_byte_144',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70db, 1, 'EVENT_3153_set_temp_action_script_sync_151']
    },
    {
        "identifier": 'EVENT_3153_jmp_145',
        "command": 'jmp',
        "args": ['EVENT_3153_set_action_script_sync_149']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_not_equals_byte_146',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70dc, 1, 'EVENT_3153_set_temp_action_script_sync_151']
    },
    {
        "identifier": 'EVENT_3153_jmp_147',
        "command": 'jmp',
        "args": ['EVENT_3153_set_action_script_sync_149']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_not_equals_byte_148',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70dd, 1, 'EVENT_3153_set_temp_action_script_sync_151']
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_149',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 7]
    },
    {
        "identifier": 'EVENT_3153_jmp_150',
        "command": 'jmp',
        "args": ['EVENT_3153_set_7010_to_object_xyz_152']
    },
    {
        "identifier": 'EVENT_3153_set_temp_action_script_sync_151',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 8]
    },
    {
        "identifier": 'EVENT_3153_set_7010_to_object_xyz_152',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_153',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3153_add_154',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_155',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_156',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_3153_mem_7000_and_const_157',
        "command": 'mem_7000_and_const',
        "args": [0x00f0]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_158',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 240, 'EVENT_3153_play_sound_192']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_159',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 160, 'EVENT_3153_play_sound_162']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_160',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_3153_play_sound_177']
    },
    {
        "identifier": 'EVENT_3153_jmp_161',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_play_sound_162',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_163',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_164',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906]
    },
    {
        "identifier": 'EVENT_3153_add_coins_165',
        "command": 'add_coins',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_166',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3153_dec_171']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_167',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3153_dec_173']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_168',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3153_dec_175']
    },
    {
        "identifier": 'EVENT_3153_dec_169',
        "command": 'dec',
        "args": [0x70da]
    },
    {
        "identifier": 'EVENT_3153_jmp_170',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_171',
        "command": 'dec',
        "args": [0x70db]
    },
    {
        "identifier": 'EVENT_3153_jmp_172',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_173',
        "command": 'dec',
        "args": [0x70dc]
    },
    {
        "identifier": 'EVENT_3153_jmp_174',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_175',
        "command": 'dec',
        "args": [0x70dd]
    },
    {
        "identifier": 'EVENT_3153_jmp_176',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_play_sound_177',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_178',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._018_SMALL_COIN, 'EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_179',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906]
    },
    {
        "identifier": 'EVENT_3153_add_coins_180',
        "command": 'add_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_181',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 1, 'EVENT_3153_dec_186']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_182',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 2, 'EVENT_3153_dec_188']
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_byte_183',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b4, 3, 'EVENT_3153_dec_190']
    },
    {
        "identifier": 'EVENT_3153_dec_184',
        "command": 'dec',
        "args": [0x70da]
    },
    {
        "identifier": 'EVENT_3153_jmp_185',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_186',
        "command": 'dec',
        "args": [0x70db]
    },
    {
        "identifier": 'EVENT_3153_jmp_187',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_188',
        "command": 'dec',
        "args": [0x70dc]
    },
    {
        "identifier": 'EVENT_3153_jmp_189',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_dec_190',
        "command": 'dec',
        "args": [0x70dd]
    },
    {
        "identifier": 'EVENT_3153_jmp_191',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_play_sound_192',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_193',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._018_SMALL_COIN, 'EVENT_3153_ret_196']
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_194',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 906]
    },
    {
        "identifier": 'EVENT_3153_add_coins_195',
        "command": 'add_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3153_ret_196',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_197',
        "command": 'set',
        "args": [0x70a7, 133]
    },
    {
        "identifier": 'EVENT_3153_set_198',
        "command": 'set',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_3153_jmp_199',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_200',
        "command": 'set',
        "args": [0x70a7, 136]
    },
    {
        "identifier": 'EVENT_3153_set_201',
        "command": 'set',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_3153_jmp_202',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_203',
        "command": 'set',
        "args": [0x70a7, 161]
    },
    {
        "identifier": 'EVENT_3153_set_204',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_3153_jmp_205',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_206',
        "command": 'set',
        "args": [0x70a7, 175]
    },
    {
        "identifier": 'EVENT_3153_set_207',
        "command": 'set',
        "args": [0x7000, 150]
    },
    {
        "identifier": 'EVENT_3153_jmp_208',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_209',
        "command": 'set',
        "args": [0x70a7, 170]
    },
    {
        "identifier": 'EVENT_3153_set_210',
        "command": 'set',
        "args": [0x7000, 100]
    },
    {
        "identifier": 'EVENT_3153_jmp_211',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_212',
        "command": 'set',
        "args": [0x70a7, 165]
    },
    {
        "identifier": 'EVENT_3153_set_213',
        "command": 'set',
        "args": [0x7000, 50]
    },
    {
        "identifier": 'EVENT_3153_jmp_214',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_set_215',
        "command": 'set',
        "args": [0x70a7, 32]
    },
    {
        "identifier": 'EVENT_3153_jmp_216',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_217',
        "command": 'set',
        "args": [0x70a7, 0]
    },
    {
        "identifier": 'EVENT_3153_jmp_218',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_219',
        "command": 'set',
        "args": [0x70a7, 48]
    },
    {
        "identifier": 'EVENT_3153_jmp_220',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_221',
        "command": 'set',
        "args": [0x70a7, 16]
    },
    {
        "identifier": 'EVENT_3153_jmp_222',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_223',
        "command": 'set',
        "args": [0x70a7, 17]
    },
    {
        "identifier": 'EVENT_3153_jmp_224',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_225',
        "command": 'set',
        "args": [0x70a7, 18]
    },
    {
        "identifier": 'EVENT_3153_jmp_226',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_227',
        "command": 'set',
        "args": [0x70a7, 19]
    },
    {
        "identifier": 'EVENT_3153_jmp_228',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_229',
        "command": 'set',
        "args": [0x70a7, 21]
    },
    {
        "identifier": 'EVENT_3153_jmp_230',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_231',
        "command": 'set',
        "args": [0x70a7, 23]
    },
    {
        "identifier": 'EVENT_3153_jmp_232',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_233',
        "command": 'set',
        "args": [0x70a7, 24]
    },
    {
        "identifier": 'EVENT_3153_jmp_234',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_235',
        "command": 'set',
        "args": [0x70a7, 25]
    },
    {
        "identifier": 'EVENT_3153_jmp_236',
        "command": 'jmp',
        "args": ['EVENT_3153_disable_trigger_34']
    },
    {
        "identifier": 'EVENT_3153_set_237',
        "command": 'set',
        "args": [0x70a7, 162]
    },
    {
        "identifier": 'EVENT_3153_set_238',
        "command": 'set',
        "args": [0x7000, 20]
    },
    {
        "identifier": 'EVENT_3153_jmp_239',
        "command": 'jmp',
        "args": ['EVENT_3153_add_coins_260']
    },
    {
        "identifier": 'EVENT_3153_ret_240',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_disable_trigger_241',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_play_sound_242',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3153_disable_event_trigger_for_object_at_70A8_243',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_244',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_3153_set_7010_to_object_xyz_245',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_246',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3153_add_247',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_248',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_bit_set_249',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'EVENT_3153_clear_bit_251']
    },
    {
        "identifier": 'EVENT_3153_play_sound_250',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_251',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'EVENT_3153_add_252',
        "command": 'add',
        "args": [0x70c8, 0x01]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_253',
        "command": 'run_dialog',
        "args": [3321, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_254',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_255',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_255_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_255_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_255_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_pause_256',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_3153_set_action_script_async_257',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_3153_set_action_script_async_258',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3153_ret_259',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_add_coins_260',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_3153_summon_to_current_level_261',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_262',
        "command": 'run_dialog',
        "args": [515, AreaObjects.MARIO, []]
    },
    {
        "identifier": 'EVENT_3153_disable_trigger_263',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_play_sound_264',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3153_disable_event_trigger_for_object_at_70A8_265',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3153_set_action_script_sync_266',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 7]
    },
    {
        "identifier": 'EVENT_3153_set_7010_to_object_xyz_267',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_268',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_3153_add_269',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_3153_set_short_mem_270',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_bit_set_271',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'EVENT_3153_clear_bit_273']
    },
    {
        "identifier": 'EVENT_3153_play_sound_272',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_273',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'EVENT_3153_create_packet_at_7010_coords_jmp_if_null_274',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_3153_ret_276']
    },
    {
        "identifier": 'EVENT_3153_jmp_275',
        "command": 'jmp',
        "args": ['EVENT_3153_ret_277']
    },
    {
        "identifier": 'EVENT_3153_ret_276',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_277',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_278',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_279',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_280',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_281',
        "command": 'set',
        "args": [0x70a7, 0]
    },
    {
        "identifier": 'EVENT_3153_set_282',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_3153_store_7000_item_quantity_to_70A7_283',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_284',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3153_set_298']
    },
    {
        "identifier": 'EVENT_3153_set_285',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_3153_store_7000_item_quantity_to_70A7_286',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_287',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3153_set_294']
    },
    {
        "identifier": 'EVENT_3153_set_288',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_3153_store_7000_item_quantity_to_70A7_289',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_3153_jmp_if_var_equals_short_290',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3153_disable_trigger_241']
    },
    {
        "identifier": 'EVENT_3153_set_291',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_3153_jmp_292',
        "command": 'jmp',
        "args": ['EVENT_3153_summon_to_current_level_22']
    },
    {
        "identifier": 'EVENT_3153_ret_293',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_294',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_3153_remove_one_from_inventory_295',
        "command": 'remove_one_from_inventory',
        "args": [items.TenorCard]
    },
    {
        "identifier": 'EVENT_3153_jmp_296',
        "command": 'jmp',
        "args": ['EVENT_3153_summon_to_current_level_22']
    },
    {
        "identifier": 'EVENT_3153_ret_297',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_set_298',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_3153_remove_one_from_inventory_299',
        "command": 'remove_one_from_inventory',
        "args": [items.AltoCard]
    },
    {
        "identifier": 'EVENT_3153_jmp_300',
        "command": 'jmp',
        "args": ['EVENT_3153_summon_to_current_level_22']
    },
    {
        "identifier": 'EVENT_3153_ret_301',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_302',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_303',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_304',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_305',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_306',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_307',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000]
    },
    {
        "identifier": 'EVENT_3153_create_packet_event_at_coords_jmp_if_null_308',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000, 'EVENT_3480_action_queue_sync_21']
    },
    {
        "identifier": 'EVENT_3153_ret_309',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_310',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3153_ret_311',
        "command": 'ret'
    }
]
