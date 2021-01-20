from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3090_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_2',
        "command": 'run_dialog',
        "args": [1548, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_3',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3090_pause_action_script_26', 'EVENT_3088_pause_action_script_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_4',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3090_run_dialog_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_6',
        "command": 'run_dialog',
        "args": [1540, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_7',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3090_pause_action_script_34', 'EVENT_3090_set_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_8',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3090_run_dialog_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_10',
        "command": 'run_dialog',
        "args": [1542, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_11',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3090_pause_action_script_111', 'EVENT_3090_pause_action_script_116'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_12',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_7000_any_bits_set_13',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3090_run_dialog_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_14',
        "command": 'run_dialog',
        "args": [1541, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_15',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3090_pause_action_script_103', 'EVENT_3090_pause_action_script_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_16',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_7000_any_bits_set_17',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3090_run_dialog_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_18',
        "command": 'run_dialog',
        "args": [1549, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_19',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3085_set_0', 'EVENT_3085_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_dialog_20',
        "command": 'run_dialog',
        "args": [1550, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_dialog_option_b_or_c_21',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3090_jmp_to_event_25', 'EVENT_3090_pause_action_script_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_22',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_23',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_to_event_25',
        "command": 'jmp_to_event',
        "args": [3812],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_26',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_27',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_open_save_menu_28',
        "command": 'open_save_menu',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_29',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_30',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_31',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_32',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_to_event_33',
        "command": 'jmp_to_event',
        "args": [3805],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_34',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_35',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_put_inventory_36',
        "command": 'put_inventory',
        "args": [items.SignalRing],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_37',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_38',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_39',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_40',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_41',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_42',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_43',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_44',
        "command": 'run_star_piece_sequence',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_45',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_46',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_47',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_48',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_49',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_50',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_51',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_52',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_53',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_54',
        "command": 'run_star_piece_sequence',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_55',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_56',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_57',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_58',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_59',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_60',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_61',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_62',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_63',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_64',
        "command": 'run_star_piece_sequence',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_65',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_66',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_67',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_68',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_69',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_70',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_71',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_72',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_73',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_74',
        "command": 'run_star_piece_sequence',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_75',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_76',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_77',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_78',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_79',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_80',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_81',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_82',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_83',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_84',
        "command": 'run_star_piece_sequence',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_85',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_86',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_87',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_88',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_89',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_90',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_db_91',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_play_music_default_volume_92',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_93',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_run_star_piece_sequence_94',
        "command": 'run_star_piece_sequence',
        "args": [6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_7000_to_pressed_button_95',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_if_var_equals_short_96',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 34, 'EVENT_3090_fade_in_from_black_async_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_97',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_3090_play_music_default_volume_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_fade_in_from_black_async_99',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_100',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_101',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_102',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_103',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_104',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_join_party_105',
        "command": 'join_party',
        "args": [AreaObjects.MALLOW],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_106',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_107',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_108',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_join_party_109',
        "command": 'join_party',
        "args": [AreaObjects.GENO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_110',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_111',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_112',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_short_party_capacity_113',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_join_party_114',
        "command": 'join_party',
        "args": [AreaObjects.TOADSTOOL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_115',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_116',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_117',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_join_party_118',
        "command": 'join_party',
        "args": [AreaObjects.BOWSER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_119',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_add_coins_120',
        "command": 'add_coins',
        "args": [99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_121',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_122',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_123',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_set_124',
        "command": 'set',
        "args": [0x7000, 999],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_add_coins_125',
        "command": 'add_coins',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_pause_action_script_126',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_enable_trigger_127',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3090_ret_128',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
