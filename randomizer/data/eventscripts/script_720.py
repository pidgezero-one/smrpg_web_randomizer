from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_0',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 205, 'EVENT_720_jmp_if_bit_set_71']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 225, 'EVENT_720_play_sound_336']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 202, 'EVENT_720_set_53']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 212, 'EVENT_720_set_211']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 215, 'EVENT_720_start_battle_229']
    },
    {
        "identifier": 'EVENT_720_restore_all_hp_5',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_720_restore_all_fp_6',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 200, 'EVENT_720_set_33']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 201, 'EVENT_720_set_41']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 203, 'EVENT_720_set_short_61']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 204, 'EVENT_720_set_short_66']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 206, 'EVENT_720_set_short_150']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 207, 'EVENT_720_set_short_155']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 208, 'EVENT_720_summon_to_level_160']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 209, 'EVENT_720_set_short_172']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 210, 'EVENT_720_set_short_177']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 211, 'EVENT_720_jmp_if_bit_set_182']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 213, 'EVENT_720_set_short_219']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 214, 'EVENT_720_set_short_224']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 216, 'EVENT_720_set_256']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 217, 'EVENT_720_set_bit_264']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 218, 'EVENT_720_set_short_300']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 219, 'EVENT_720_set_short_305']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 220, 'EVENT_720_set_short_310']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 221, 'EVENT_720_set_short_315']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 222, 'EVENT_720_set_short_320']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_325']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_27',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 224, 'EVENT_720_set_short_331']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_28',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 226, 'EVENT_720_set_short_368']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_29',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 227, 'EVENT_720_set_short_383']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_30',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 228, 'EVENT_720_set_short_388']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 229, 'EVENT_720_set_short_393']
    },
    {
        "identifier": 'EVENT_720_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_33',
        "command": 'set',
        "args": [0x70a7, 5]
    },
    {
        "identifier": 'EVENT_720_set_short_34',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_35',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_36',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_38',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_39',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_41',
        "command": 'set',
        "args": [0x70a7, 128]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_42',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_720_set_613']
    },
    {
        "identifier": 'EVENT_720_set_short_43',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_44',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_45',
        "command": 'set',
        "args": [0x70a7, 129]
    },
    {
        "identifier": 'EVENT_720_set_short_46',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_47',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_48',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_49',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_50',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_51',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_52',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_53',
        "command": 'set',
        "args": [0x70a7, 87]
    },
    {
        "identifier": 'EVENT_720_set_short_54',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_55',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_56',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_57',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_58',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_59',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_60',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_61',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_62',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_63',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_64',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_65',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_66',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_67',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_68',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_69',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_70',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_71',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'EVENT_720_set_93']
    },
    {
        "identifier": 'EVENT_720_set_bit_72',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_start_battle_73',
        "command": 'start_battle',
        "args": [0x00a4, 5]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_74',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_720_reset_and_choose_game_366']
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_75',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_stop_sound_76',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_stop_sound_77',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_set_bit_78',
        "command": 'set_bit',
        "args": [0x7056, 5]
    },
    {
        "identifier": 'EVENT_720_restore_all_hp_79',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_720_restore_all_fp_80',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_720_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_object_memory_set_bit_6',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_81_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_resume_action_script_82',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_720_set_7000_to_current_level_83',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_not_equals_short_84',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 277, 'EVENT_720_jmp_if_var_not_equals_short_87']
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_85',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 6, 'EVENT_720_set_93']
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_86_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_86_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_720_action_queue_sync_106_SUBSCRIPT_object_memory_set_bit_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_not_equals_short_87',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 283, 'EVENT_720_jmp_if_var_not_equals_short_90']
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_88',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 7, 'EVENT_720_set_93']
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_89_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_89_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_720_action_queue_sync_122_SUBSCRIPT_object_memory_set_bit_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_not_equals_short_90',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 273, 'EVENT_720_set_93']
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_91',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 0, 'EVENT_720_set_93']
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_92_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_92_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_720_set_93',
        "command": 'set',
        "args": [0x70a7, 135]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_94',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 151, 'EVENT_720_set_613']
    },
    {
        "identifier": 'EVENT_720_set_short_95',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_96',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_97',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_98',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_99',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_100',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_101',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_move_script_to_main_thread_102',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_720_set_bit_103',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_set_short_104',
        "command": 'set_short',
        "args": [0x700e, 0x008d]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_105',
        "command": 'run_event_as_subroutine',
        "args": [18]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_jmp_if_bit_clear_11',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_shift_southeast_steps_18',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_shift_southeast_steps_20',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_visibility_off_21',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_object_memory_set_bit_22',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_106_SUBSCRIPT_ret_23',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_run_dialog_107',
        "command": 'run_dialog',
        "args": [1644, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_720_set_bit_108',
        "command": 'set_bit',
        "args": [0x7056, 6]
    },
    {
        "identifier": 'EVENT_720_set_bit_109',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_110',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_720_close_dialog_115']
    },
    {
        "identifier": 'EVENT_720_set_111',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_720_play_sound_112',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_720_run_dialog_113',
        "command": 'run_dialog',
        "args": [1645, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_720_put_inventory_114',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_720_close_dialog_115',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_720_clear_bit_116',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_ret_117',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_move_script_to_main_thread_118',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_720_set_bit_119',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_set_short_120',
        "command": 'set_short',
        "args": [0x700e, 0x008d]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_121',
        "command": 'run_event_as_subroutine',
        "args": [18]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_jmp_if_bit_clear_11',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_shift_northwest_steps_18',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_shift_northwest_steps_20',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_visibility_off_21',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_object_memory_set_bit_22',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_122_SUBSCRIPT_ret_23',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_run_dialog_123',
        "command": 'run_dialog',
        "args": [1644, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_720_set_bit_124',
        "command": 'set_bit',
        "args": [0x7056, 7]
    },
    {
        "identifier": 'EVENT_720_set_bit_125',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_126',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_720_close_dialog_131']
    },
    {
        "identifier": 'EVENT_720_set_127',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_720_play_sound_128',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_720_run_dialog_129',
        "command": 'run_dialog',
        "args": [1645, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_720_put_inventory_130',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_720_close_dialog_131',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_720_clear_bit_132',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_ret_133',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_move_script_to_main_thread_134',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_720_set_bit_135',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_set_short_136',
        "command": 'set_short',
        "args": [0x700e, 0x008d]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_137',
        "command": 'run_event_as_subroutine',
        "args": [18]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_jmp_if_bit_clear_11',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_object_memory_set_bit_16',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_shift_southeast_steps_18',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_shift_northeast_steps_19',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_object_memory_set_bit_21',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_138_SUBSCRIPT_ret_22',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_run_dialog_139',
        "command": 'run_dialog',
        "args": [1644, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_720_set_bit_140',
        "command": 'set_bit',
        "args": [0x7057, 0]
    },
    {
        "identifier": 'EVENT_720_set_bit_141',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_142',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_720_close_dialog_147']
    },
    {
        "identifier": 'EVENT_720_set_143',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_720_play_sound_144',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_720_run_dialog_145',
        "command": 'run_dialog',
        "args": [1645, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_720_put_inventory_146',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_720_close_dialog_147',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_720_clear_bit_148',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_720_ret_149',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_150',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_151',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_152',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_153',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_154',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_155',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_156',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_157',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_158',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_159',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_summon_to_level_160',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_summon_to_level_161',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_summon_to_level_162',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_remove_from_level_163',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_remove_from_level_164',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_remove_from_level_165',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_remove_from_level_166',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_720_set_short_167',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_168',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_169',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_170',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_171',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_172',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_173',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_174',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_175',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_176',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_177',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_178',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_179',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_180',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_181',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_182',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 6, 'EVENT_720_fade_out_to_black_async_200']
    },
    {
        "identifier": 'EVENT_720_start_battle_183',
        "command": 'start_battle',
        "args": [0x00a7, 3]
    },
    {
        "identifier": 'EVENT_720_set_bit_184',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_720_clear_bit_185',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_720_clear_bit_186',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_187',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_720_restore_all_hp_188',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_720_restore_all_fp_189',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_720_set_bit_190',
        "command": 'set_bit',
        "args": [0x7058, 6]
    },
    {
        "identifier": 'EVENT_720_enter_area_191',
        "command": 'enter_area',
        "args": [Rooms._173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, RadialDirections.NORTHEAST, 3, 89, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_720_clear_bit_192',
        "command": 'clear_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_193',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_193_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_pause_194',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_720_set_short_195',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_196',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_197',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_198',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_199',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_fade_out_to_black_async_200',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_720_stop_sound_201',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_stop_sound_202',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_stop_sound_203',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_stop_sound_204',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_set_bit_205',
        "command": 'set_bit',
        "args": [0x7049, 0]
    },
    {
        "identifier": 'EVENT_720_enable_controls_206',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_720_enter_area_207',
        "command": 'enter_area',
        "args": [Rooms._173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, RadialDirections.SOUTH, 2, 92, 8, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_208',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_208_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_ret_209',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_ret_210',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_211',
        "command": 'set',
        "args": [0x70a7, 75]
    },
    {
        "identifier": 'EVENT_720_set_short_212',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_213',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_214',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_215',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_216',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_217',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_218',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_219',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_220',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_221',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_222',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_223',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_224',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_225',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_226',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_227',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_228',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_start_battle_229',
        "command": 'start_battle',
        "args": [0x00a9, 42]
    },
    {
        "identifier": 'EVENT_720_set_bit_230',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_720_set_bit_231',
        "command": 'set_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_720_set_bit_232',
        "command": 'set_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_233',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_720_remove_from_current_level_234',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_720_restore_all_hp_235',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_720_restore_all_fp_236',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_237',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_play_sound_238',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_720_set_short_239',
        "command": 'set_short',
        "args": [0x7034, 0x0001]
    },
    {
        "identifier": 'EVENT_720_set_7010_to_object_xyz_240',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_720_start_loop_n_times_241',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_720_pause_242',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_720_create_packet_at_7010_coords_jmp_if_null_243',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_720_pause_242']
    },
    {
        "identifier": 'EVENT_720_pause_244',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_720_add_short_245',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_720_end_loop_246',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_247',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_247_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_summon_to_level_248',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._324_MONSTRO_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_720_set_short_249',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_set_bit_250',
        "command": 'set_bit',
        "args": [0x708a, 0]
    },
    {
        "identifier": 'EVENT_720_set_bit_251',
        "command": 'set_bit',
        "args": [0x7068, 0]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_252',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_253',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_254',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_255',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_256',
        "command": 'set',
        "args": [0x70a7, 90]
    },
    {
        "identifier": 'EVENT_720_set_short_257',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_258',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_259',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_260',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_261',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_262',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_263',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_bit_264',
        "command": 'set_bit',
        "args": [0x7093, 5]
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_265',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_266',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 6, 'EVENT_720_set_bit_275']
    },
    {
        "identifier": 'EVENT_720_set_short_mem_267',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70bd]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_268',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_720_action_queue_async_270']
    },
    {
        "identifier": 'EVENT_720_action_queue_async_269',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_269_SUBSCRIPT_load_mem_0',
                "command": 'load_mem',
                "args": [0x7000]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_269_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_269_SUBSCRIPT_end_loop_2',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_action_queue_async_270',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_270_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_271',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_720_enable_controls_until_return_281']
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_272',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_273',
        "command": 'jmp',
        "args": ['EVENT_720_set_292']
    },
    {
        "identifier": 'EVENT_720_ret_274',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_bit_275',
        "command": 'set_bit',
        "args": [0x7088, 6]
    },
    {
        "identifier": 'EVENT_720_action_queue_async_276',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_276_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 62, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_276_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_277',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7044, 7, 'EVENT_720_enable_controls_until_return_281']
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_278',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_279',
        "command": 'jmp',
        "args": ['EVENT_720_set_292']
    },
    {
        "identifier": 'EVENT_720_ret_280',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_enable_controls_until_return_281',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_720_freeze_camera_282',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_720_action_queue_async_283',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_face_south_3',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_floating_off_4',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_283_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_284',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_action_queue_async_285',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_720_action_queue_async_285_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_object_memory_set_bit_3',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_shadow_off_5',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [165]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_walk_1_step_south_9',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_jmp_if_mario_in_air_11',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_720_action_queue_async_285_SUBSCRIPT_pause_10']
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_object_memory_clear_bit_12',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_async_285_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_set_action_script_async_286',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_720_unfreeze_camera_287',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_720_enable_controls_until_return_288',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_720_clear_bit_289',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_720_jmp_290',
        "command": 'jmp',
        "args": ['EVENT_720_set_292']
    },
    {
        "identifier": 'EVENT_720_ret_291',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_292',
        "command": 'set',
        "args": [0x70a7, 94]
    },
    {
        "identifier": 'EVENT_720_set_short_293',
        "command": 'set_short',
        "args": [0x7000, 0x020c]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_294',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_set_short_295',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_296',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_297',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_298',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_299',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_300',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_301',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_302',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_303',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_304',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_305',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_306',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_307',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_308',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_309',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_310',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_311',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_312',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_313',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_314',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_315',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_316',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_317',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_318',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_319',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_320',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_321',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_322',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_323',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_324',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_325',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_326',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_327',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_328',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_open_location_329',
        "command": 'open_location',
        "args": [Locations._050_BARREL_VOLCANO, []]
    },
    {
        "identifier": 'EVENT_720_ret_330',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_331',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_332',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_333',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_334',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_335',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_sound_336',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_720_set_short_mem_337',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_720_set_short_mem_338',
        "command": 'set_short_mem',
        "args": [0x70b4, 0x7000]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_339',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_339_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_339_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_340',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_340_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_set_7010_to_object_xyz_341',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_720_set_short_mem_342',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_720_add_343',
        "command": 'add',
        "args": [0x7000, 608]
    },
    {
        "identifier": 'EVENT_720_set_short_mem_344',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_720_clear_bit_345',
        "command": 'clear_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_720_play_sound_346',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_720_create_packet_at_7010_coords_jmp_if_null_347',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._004_MONSTER_FACE, 'EVENT_720_pause_348']
    },
    {
        "identifier": 'EVENT_720_pause_348',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_720_stop_embedded_action_script_349',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_720_start_battle_350',
        "command": 'start_battle',
        "args": [0x009e, 21]
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_351',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_720_reset_and_choose_game_366']
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_352',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_352_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_352_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_353',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_set_bit_354',
        "command": 'set_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_720_set_bit_355',
        "command": 'set_bit',
        "args": [0x7064, 5]
    },
    {
        "identifier": 'EVENT_720_action_queue_sync_356',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_object_memory_set_bit_5',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_720_action_queue_sync_356_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_720_remove_from_level_357',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_720_summon_to_level_358',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_720_stop_embedded_action_script_359',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_720_set_action_script_async_360',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 15]
    },
    {
        "identifier": 'EVENT_720_set_short_361',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_362',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_363',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_364',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_365',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_reset_and_choose_game_366',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_720_ret_367',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_368',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_369',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_370',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_371',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_372',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_373',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_374',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_375',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_376',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_377',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_378',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_379',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_380',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_381',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_382',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_383',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_384',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_385',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_386',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_387',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_388',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_389',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_390',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_391',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_392',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_short_393',
        "command": 'set_short',
        "args": [0x71fe, 0x00ff]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_394',
        "command": 'jmp_if_var_equals_short',
        "args": [0x71fe, 255, 'EVENT_720_jmp_if_bit_set_398']
    },
    {
        "identifier": 'EVENT_720_set_short_395',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_396',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_397',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_398',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 1, 'EVENT_720_jmp_if_var_equals_byte_400']
    },
    {
        "identifier": 'EVENT_720_set_bit_399',
        "command": 'set_bit',
        "args": [0x7062, 1]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_400',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 6, 'EVENT_720_jmp_if_bit_clear_478']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_401',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 5, 'EVENT_720_add_463']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_402',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 4, 'EVENT_720_add_452']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_403',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 3, 'EVENT_720_add_441']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_404',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 2, 'EVENT_720_add_430']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_405',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 1, 'EVENT_720_add_419']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_byte_406',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 0, 'EVENT_720_add_408']
    },
    {
        "identifier": 'EVENT_720_ret_407',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_408',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_409',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_410',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_411',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_412',
        "command": 'run_star_piece_sequence',
        "args": [1]
    },
    {
        "identifier": 'EVENT_720_db_413',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_414',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_415',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_416',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_417',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_418',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_419',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_420',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_421',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_422',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_423',
        "command": 'run_star_piece_sequence',
        "args": [2]
    },
    {
        "identifier": 'EVENT_720_db_424',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_425',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_426',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_427',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_428',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_429',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_430',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_431',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_432',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_433',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_434',
        "command": 'run_star_piece_sequence',
        "args": [3]
    },
    {
        "identifier": 'EVENT_720_db_435',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_436',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_437',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_438',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_439',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_440',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_441',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_442',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_443',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_444',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_445',
        "command": 'run_star_piece_sequence',
        "args": [4]
    },
    {
        "identifier": 'EVENT_720_db_446',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_447',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_448',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_449',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_450',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_451',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_452',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_453',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_454',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_455',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_456',
        "command": 'run_star_piece_sequence',
        "args": [5]
    },
    {
        "identifier": 'EVENT_720_db_457',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_458',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_459',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_460',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_461',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_462',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_add_463',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_464',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_465',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_466',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_467',
        "command": 'run_star_piece_sequence',
        "args": [6]
    },
    {
        "identifier": 'EVENT_720_db_468',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_469',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_470',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_720_jmp_if_bit_clear_499']
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_471',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 1, 'EVENT_720_fade_in_from_black_async_510']
    },
    {
        "identifier": 'EVENT_720_set_bit_472',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_720_set_bit_473',
        "command": 'set_bit',
        "args": [0x7070, 7]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_474',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_475',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_476',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_477',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_clear_478',
        "command": 'jmp_if_bit_clear',
        "args": [0x7098, 1, 'EVENT_720_ret_492']
    },
    {
        "identifier": 'EVENT_720_add_479',
        "command": 'add',
        "args": [0x70d5, 0x01]
    },
    {
        "identifier": 'EVENT_720_play_music_current_volume_480',
        "command": 'play_music_current_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_720_db_481',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_482',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_run_star_piece_sequence_483',
        "command": 'run_star_piece_sequence',
        "args": [7]
    },
    {
        "identifier": 'EVENT_720_db_484',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_720_pause_script_until_effect_done_485',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_set_486',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_720_set_bit_493']
    },
    {
        "identifier": 'EVENT_720_set_bit_487',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_720_set_bit_488',
        "command": 'set_bit',
        "args": [0x7070, 7]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_489',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_490',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_491',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_492',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_bit_493',
        "command": 'set_bit',
        "args": [0x7070, 5]
    },
    {
        "identifier": 'EVENT_720_set_bit_494',
        "command": 'set_bit',
        "args": [0x7068, 5]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_495',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_496',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_497',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_498',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_bit_clear_499',
        "command": 'jmp_if_bit_clear',
        "args": [0x7098, 1, 'EVENT_720_set_bit_504']
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_500',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_501',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_502',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_503',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_bit_504',
        "command": 'set_bit',
        "args": [0x7070, 5]
    },
    {
        "identifier": 'EVENT_720_set_bit_505',
        "command": 'set_bit',
        "args": [0x7068, 5]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_506',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_507',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_508',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_509',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_510',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_511',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_512',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_513',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_bit_514',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_720_set_bit_515',
        "command": 'set_bit',
        "args": [0x7070, 5]
    },
    {
        "identifier": 'EVENT_720_fade_in_from_black_async_516',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_517',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 223, 'EVENT_720_set_short_327']
    },
    {
        "identifier": 'EVENT_720_jmp_518',
        "command": 'jmp',
        "args": ['EVENT_720_jmp_if_var_equals_short_520']
    },
    {
        "identifier": 'EVENT_720_ret_519',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_520',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 202, 'EVENT_720_play_music_default_volume_561']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_521',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 204, 'EVENT_720_play_music_default_volume_565']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_522',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 205, 'EVENT_720_play_music_default_volume_561']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_523',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 206, 'EVENT_720_play_music_default_volume_561']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_524',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 207, 'EVENT_720_play_music_default_volume_569']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_525',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 208, 'EVENT_720_play_music_default_volume_549']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_526',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 209, 'EVENT_720_play_music_default_volume_577']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_527',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 210, 'EVENT_720_play_music_default_volume_581']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_528',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 211, 'EVENT_720_play_music_default_volume_585']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_529',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 212, 'EVENT_720_play_music_default_volume_585']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_530',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 213, 'EVENT_720_play_music_default_volume_585']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_531',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 214, 'EVENT_720_play_music_default_volume_589']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_532',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 215, 'EVENT_720_play_music_default_volume_561']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_533',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 216, 'EVENT_720_play_music_default_volume_605']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_534',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 217, 'EVENT_720_play_music_default_volume_605']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_535',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 218, 'EVENT_720_play_music_default_volume_553']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_536',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 219, 'EVENT_720_play_music_default_volume_593']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_537',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 220, 'EVENT_720_play_music_default_volume_593']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_538',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 221, 'EVENT_720_play_music_default_volume_597']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_539',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 222, 'EVENT_720_play_music_default_volume_601']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_540',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 224, 'EVENT_720_play_music_default_volume_557']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_541',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 225, 'EVENT_720_play_music_default_volume_553']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_542',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 226, 'EVENT_720_play_music_default_volume_605']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_543',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 227, 'EVENT_720_play_music_default_volume_609']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_544',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 228, 'EVENT_720_play_music_default_volume_609']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_545',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 229, 'EVENT_720_play_music_default_volume_609']
    },
    {
        "identifier": 'EVENT_720_set_short_546',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_547',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_548',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_549',
        "command": 'play_music_default_volume',
        "args": [Music._13_ROAD_IS_FULL_OF_DANGERS]
    },
    {
        "identifier": 'EVENT_720_set_short_550',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_551',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_552',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_553',
        "command": 'play_music_default_volume',
        "args": [Music._42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": 'EVENT_720_set_short_554',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_555',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_556',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_557',
        "command": 'play_music_default_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_720_set_short_558',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_559',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_560',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_561',
        "command": 'play_music_default_volume',
        "args": [Music._27_DUNGEON_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": 'EVENT_720_set_short_562',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_563',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_564',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_565',
        "command": 'play_music_default_volume',
        "args": [Music._26_FOREST_MAZE]
    },
    {
        "identifier": 'EVENT_720_set_short_566',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_567',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_568',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_569',
        "command": 'play_music_default_volume',
        "args": [Music._31_BOOSTERS_TOWER]
    },
    {
        "identifier": 'EVENT_720_set_short_570',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_571',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_572',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_573',
        "command": 'play_music_default_volume',
        "args": [Music._13_ROAD_IS_FULL_OF_DANGERS]
    },
    {
        "identifier": 'EVENT_720_set_short_574',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_575',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_576',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_577',
        "command": 'play_music_default_volume',
        "args": [Music._39_MARRYMORE]
    },
    {
        "identifier": 'EVENT_720_set_short_578',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_579',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_580',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_581',
        "command": 'play_music_default_volume',
        "args": [Music._34_STAR_HILL]
    },
    {
        "identifier": 'EVENT_720_set_short_582',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_583',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_584',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_585',
        "command": 'play_music_default_volume',
        "args": [Music._41_SUNKEN_SHIP]
    },
    {
        "identifier": 'EVENT_720_set_short_586',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_587',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_588',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_589',
        "command": 'play_music_default_volume',
        "args": [Music._05_SEASIDE_TOWN]
    },
    {
        "identifier": 'EVENT_720_set_short_590',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_591',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_592',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_593',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA]
    },
    {
        "identifier": 'EVENT_720_set_short_594',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_595',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_596',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_597',
        "command": 'play_music_default_volume',
        "args": [Music._50_NIMBUS_LAND]
    },
    {
        "identifier": 'EVENT_720_set_short_598',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_599',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_600',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_601',
        "command": 'play_music_default_volume',
        "args": [Music._62_BARREL_VOLCANO]
    },
    {
        "identifier": 'EVENT_720_set_short_602',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_603',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_604',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_605',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN]
    },
    {
        "identifier": 'EVENT_720_set_short_606',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_607',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_608',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_play_music_default_volume_609',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": 'EVENT_720_set_short_610',
        "command": 'set_short',
        "args": [0x700a, 0x0000]
    },
    {
        "identifier": 'EVENT_720_set_short_611',
        "command": 'set_short',
        "args": [0x71fe, 0x0000]
    },
    {
        "identifier": 'EVENT_720_ret_612',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_613',
        "command": 'set',
        "args": [0x70a7, 0]
    },
    {
        "identifier": 'EVENT_720_set_614',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_720_store_7000_item_quantity_to_70A7_615',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_616',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_720_set_626']
    },
    {
        "identifier": 'EVENT_720_set_617',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_720_store_7000_item_quantity_to_70A7_618',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_619',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_720_set_633']
    },
    {
        "identifier": 'EVENT_720_set_620',
        "command": 'set',
        "args": [0x70a7, 151]
    },
    {
        "identifier": 'EVENT_720_set_621',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_622',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_623',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 201, 'EVENT_720_set_45']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_624',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 205, 'EVENT_720_set_short_97']
    },
    {
        "identifier": 'EVENT_720_ret_625',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_626',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_720_set_627',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_628',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_remove_one_from_inventory_629',
        "command": 'remove_one_from_inventory',
        "args": [items.AltoCard]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_630',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 201, 'EVENT_720_set_45']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_631',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 205, 'EVENT_720_set_short_97']
    },
    {
        "identifier": 'EVENT_720_ret_632',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_set_633',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_720_set_634',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_720_run_event_as_subroutine_635',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_720_remove_one_from_inventory_636',
        "command": 'remove_one_from_inventory',
        "args": [items.TenorCard]
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_637',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 201, 'EVENT_720_set_45']
    },
    {
        "identifier": 'EVENT_720_jmp_if_var_equals_short_638',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700a, 205, 'EVENT_720_set_short_97']
    },
    {
        "identifier": 'EVENT_720_ret_639',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_640',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc72e]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_641',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x29db]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_642',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8c8f]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_643',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xef35]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_644',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x51cd]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_645',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb46c]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_646',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x16f6]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_647',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7987]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_648',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xdc0a]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_649',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3e7f]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_650',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa0fb]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_651',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x0362]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_652',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x65d5]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_653',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc830]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_654',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2a82]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_655',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8cdb]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_656',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xef26]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_657',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5163]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_658',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xb3a7]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_659',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x15d6]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_660',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x780c]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_661',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xda34]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_662',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x3c4e]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_663',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9e77]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_664',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x007b]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_665',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x62a2]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_666',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc493]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_667',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x268a]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_668',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8888]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_669',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xea78]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_670',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4c5a]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_671',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xae43]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_672',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x1017]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_673',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x71f2]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_674',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd3bf]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_675',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x357e]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_676',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x9b3b]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_677',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xf8f5]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_678',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x5aad]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_679',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xbc57]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_680',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x7f96]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_681',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xe12b]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_682',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x42b2]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_683',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xa440]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_684',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x05b9]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_685',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x6739]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_686',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xc8ab]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_687',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x2a0f]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_688',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x8b7a]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_689',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xecd7]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_690',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x4e26]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_691',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xaf7c]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_692',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0x10bd]
    },
    {
        "identifier": 'EVENT_720_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_693',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.MARIO, AreaObjects.MARIO, 0x00, 0x00, 0xd33f]
    },
    {
        "identifier": 'EVENT_720_stop_sound_694',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_720_ret_695',
        "command": 'ret'
    }
]
