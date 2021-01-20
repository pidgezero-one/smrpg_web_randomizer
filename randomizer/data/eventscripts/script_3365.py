from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3365_resume_action_script_0',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 4, 'EVENT_3365_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 1, 'EVENT_3365_run_dialog_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_5',
        "command": 'run_dialog',
        "args": [1932, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3365_set_bit_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_7',
        "command": 'run_dialog',
        "args": [1933, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_8',
        "command": 'set',
        "args": [0x70af, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_11',
        "command": 'run_dialog',
        "args": [1935, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_12',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_14',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_15',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_16',
        "command": 'run_dialog',
        "args": [1921, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_19',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_20',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_21',
        "command": 'run_dialog',
        "args": [1922, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_24',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_25',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_26',
        "command": 'run_dialog',
        "args": [1923, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7032],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_29',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_30',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_add_short_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_31',
        "command": 'run_dialog',
        "args": [1924, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_add_short_32',
        "command": 'add_short',
        "args": [0x7034, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_33',
        "command": 'mem_compare',
        "args": [0x7034, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_0_34',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_3365_mem_compare_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_35',
        "command": 'run_dialog',
        "args": [1936, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_36',
        "command": 'mem_compare',
        "args": [0x7034, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_37',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_38',
        "command": 'run_dialog',
        "args": [1937, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_bit_39',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_dialog_option_b_40',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3365_clear_bit_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_3365_set_short_mem_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_42',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_43',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_45',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_46',
        "command": 'set',
        "args": [0x70ae, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_47',
        "command": 'set',
        "args": [0x70af, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_ret_48',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_50',
        "command": 'mem_compare',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_51',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_play_sound_78'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_52',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_53',
        "command": 'mem_compare',
        "args": [0x7000, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_54',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_play_sound_78'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_55',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_56',
        "command": 'mem_compare',
        "args": [0x7000, 0x7030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_57',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_play_sound_78'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_59',
        "command": 'mem_compare',
        "args": [0x7000, 0x7032],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_60',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_play_sound_78'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_pause_61',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_clear_bit_62',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_play_sound_64',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_pause_65',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_play_music_default_volume_66',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_67',
        "command": 'run_dialog',
        "args": [1938, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_bit_68',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_object_memory_set_bit_8',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_69_SUBSCRIPT_end_all_9',
                "command": 'end_all',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_sync_70_SUBSCRIPT_jmp_0',
                "command": 'jmp',
                "args": ['EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0']
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_sync_71_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3365_action_queue_sync_71_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0']
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_sync_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3365_action_queue_sync_72_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0']
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_async_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_73_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0']
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_play_sound_74',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_apply_tile_mod_75',
        "command": 'apply_tile_mod',
        "args": [Rooms._466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_apply_solidity_mod_76',
        "command": 'apply_solidity_mod',
        "args": [Rooms._466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_ret_77',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_play_sound_78',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_pause_79',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_play_music_default_volume_80',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_slow_down_music_81',
        "command": 'slow_down_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3365_action_queue_async_82_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3365_action_queue_async_82_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3365_clear_bit_83',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_85',
        "command": 'run_dialog',
        "args": [1939, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_86',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_87',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_88',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_89',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_92'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_90',
        "command": 'run_dialog',
        "args": [1921, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_91',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_92',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_93',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_94',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_95',
        "command": 'run_dialog',
        "args": [1922, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_96',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_97',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_98',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_99',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_102'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_100',
        "command": 'run_dialog',
        "args": [1923, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_3365_add_short_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_short_mem_102',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_103',
        "command": 'mem_compare',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_104',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_add_short_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_105',
        "command": 'run_dialog',
        "args": [1924, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_add_short_106',
        "command": 'add_short',
        "args": [0x7034, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_107',
        "command": 'mem_compare',
        "args": [0x7034, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_0_108',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_3365_mem_compare_110'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_109',
        "command": 'run_dialog',
        "args": [1936, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_mem_compare_110',
        "command": 'mem_compare',
        "args": [0x7034, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_if_loaded_memory_is_not_0_111',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3365_set_short_mem_87'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_run_dialog_112',
        "command": 'run_dialog',
        "args": [1940, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_set_bit_113',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_pause_114',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_fade_out_to_black_async_115',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3365_jmp_to_event_116',
        "command": 'jmp_to_event',
        "args": [3356],
        "subscript": []
    },
]
