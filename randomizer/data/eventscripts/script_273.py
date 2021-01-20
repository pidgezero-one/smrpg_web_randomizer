from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_273_run_dialog_0',
        "command": 'run_dialog',
        "args": [519, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_dialog_option_b_1',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_273_run_event_as_subroutine_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_273_run_event_as_subroutine_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_5',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_dialog_6',
        "command": 'run_dialog',
        "args": [521, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_273_clear_bit_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_10',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_bit_11',
        "command": 'set_bit',
        "args": [0x7049, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_event_as_subroutine_12',
        "command": 'run_event_as_subroutine',
        "args": [274],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_273_clear_bit_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_close_dialog_14',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_dec_coins_16',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_fade_out_music_to_volume_17',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_circle_mask_static_18',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 18, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_19',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_21',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_pause_23',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_circle_mask_static_24',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_script_until_effect_done_25',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_bit_26',
        "command": 'set_bit',
        "args": [0x7049, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_to_subroutine_27',
        "command": 'jmp_to_subroutine',
        "args": [0x105a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_restore_all_hp_28',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_restore_all_fp_29',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_pause_31',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._029_ALARM_CLOCK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_33',
        "command": 'pause',
        "args": [92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_35',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_36_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._047_SNOOZE, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_circle_mask_static_37',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 255, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_script_until_effect_done_38',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_39',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_fade_out_music_to_volume_40',
        "command": 'fade_out_music_to_volume',
        "args": [2, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_41',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_stop_sound_42',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_run_event_as_subroutine_44',
        "command": 'run_event_as_subroutine',
        "args": [286],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": [0x1159],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_action_script_46',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_273_action_queue_async_47_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_273_action_queue_async_47_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7049, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x7084, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7084, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_51',
        "command": 'clear_bit',
        "args": [0x7061, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_52',
        "command": 'clear_bit',
        "args": [0x705e, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_53',
        "command": 'clear_bit',
        "args": [0x7062, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_54',
        "command": 'clear_bit',
        "args": [0x7062, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7062, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7062, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_57',
        "command": 'clear_bit',
        "args": [0x705d, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_58',
        "command": 'clear_bit',
        "args": [0x7049, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7049, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_60',
        "command": 'clear_bit',
        "args": [0x7090, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_62',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_273_action_queue_sync_163'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_63',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_64',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 5, 'EVENT_273_enter_area_77'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_65',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 6, 'EVENT_273_enter_area_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_66',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 1, 'EVENT_273_enter_area_89'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 3, 'EVENT_273_enter_area_96'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 4, 'EVENT_273_enter_area_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_69',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 5, 'EVENT_273_enter_area_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_70',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 6, 'EVENT_273_enter_area_111'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_71',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 7, 'EVENT_273_enter_area_115'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_72',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 6, 'EVENT_273_enter_area_118'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_73',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 7, 'EVENT_273_enter_area_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_74',
        "command": 'enter_area',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, RadialDirections.SOUTH, 6, 119, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_75',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_76',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_77',
        "command": 'enter_area',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, RadialDirections.SOUTH, 6, 119, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_78',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_79',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_80',
        "command": 'enter_area',
        "args": [Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F, RadialDirections.SOUTH, 6, 43, 3, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_81',
        "command": 'apply_tile_mod',
        "args": [Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_82_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_clear_83',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 0, 'EVENT_273_ret_88'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_84',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 2, 'EVENT_273_ret_88'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_bit_85',
        "command": 'set_bit',
        "args": [0x7060, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_summon_to_current_level_86',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_action_script_sync_87',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_88',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_89',
        "command": 'enter_area',
        "args": [Rooms._096_ROSE_TOWN_INN_2F, RadialDirections.SOUTH, 6, 43, 3, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_90',
        "command": 'apply_tile_mod',
        "args": [Rooms._096_ROSE_TOWN_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_91_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_set_bit_92',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_93_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_93_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_94',
        "command": 'apply_tile_mod',
        "args": [Rooms._096_ROSE_TOWN_INN_2F, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_95',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_96',
        "command": 'enter_area',
        "args": [Rooms._337_MOLEVILLE_INN, RadialDirections.SOUTH, 6, 11, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_97',
        "command": 'apply_tile_mod',
        "args": [Rooms._337_MOLEVILLE_INN, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_98',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_99',
        "command": 'enter_area',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, RadialDirections.SOUTH, 17, 12, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_100',
        "command": 'apply_tile_mod',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_object_not_in_level_101',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_273_jmp_if_object_trigger_disabled_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_102',
        "command": 'apply_tile_mod',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_object_trigger_disabled_103',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 'EVENT_273_ret_105'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_104_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_ret_105',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_106',
        "command": 'enter_area',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, RadialDirections.SOUTH, 8, 13, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_107',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_108_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_clear_bit_109',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_110',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_111',
        "command": 'enter_area',
        "args": [Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, RadialDirections.SOUTH, 6, 73, 3, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_112',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_112_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 78, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_112_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_113',
        "command": 'apply_tile_mod',
        "args": [Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_114',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_115',
        "command": 'enter_area',
        "args": [Rooms._306_SEASIDE_TOWN_INN_2F, RadialDirections.SOUTH, 6, 73, 3, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_116',
        "command": 'apply_tile_mod',
        "args": [Rooms._306_SEASIDE_TOWN_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_117',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_118',
        "command": 'enter_area',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, RadialDirections.SOUTH, 6, 119, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_119',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_120',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_enter_area_121',
        "command": 'enter_area',
        "args": [Rooms._346_NIMBUS_LAND_INN_BEDROOM, RadialDirections.SOUTH, 15, 79, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_122',
        "command": 'apply_tile_mod',
        "args": [Rooms._346_NIMBUS_LAND_INN_BEDROOM, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_clear_123',
        "command": 'jmp_if_bit_clear',
        "args": [0x707d, 7, 'EVENT_273_jmp_if_bit_set_127'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_summon_to_current_level_124',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_125',
        "command": 'apply_tile_mod',
        "args": [Rooms._346_NIMBUS_LAND_INN_BEDROOM, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_126_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_126_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [17, 83, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_126_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [250, 250, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_127',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_273_summon_to_current_level_129'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_128',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_summon_to_current_level_129',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_130',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_131',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 5, 'EVENT_273_apply_tile_mod_143'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_132',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 6, 'EVENT_273_apply_tile_mod_145'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_133',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 1, 'EVENT_273_apply_tile_mod_147'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_134',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 3, 'EVENT_273_apply_tile_mod_149'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_135',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 4, 'EVENT_273_apply_tile_mod_151'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_136',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 5, 'EVENT_273_apply_tile_mod_153'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_137',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 6, 'EVENT_273_apply_tile_mod_155'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_138',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 7, 'EVENT_273_apply_tile_mod_157'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_139',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 6, 'EVENT_273_apply_tile_mod_159'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_jmp_if_bit_set_140',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 7, 'EVENT_273_apply_tile_mod_161'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_141',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_142',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_143',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_144',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_145',
        "command": 'apply_tile_mod',
        "args": [Rooms._095_ROSE_TOWN_DURING_BOWYER_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_146',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_147',
        "command": 'apply_tile_mod',
        "args": [Rooms._096_ROSE_TOWN_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_148',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_149',
        "command": 'apply_tile_mod',
        "args": [Rooms._337_MOLEVILLE_INN, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_150',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_151',
        "command": 'apply_tile_mod',
        "args": [Rooms._009_MARRYMORE_INN_REGULAR_ROOM, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_152',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_153',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_154',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_155',
        "command": 'apply_tile_mod',
        "args": [Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_156',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_157',
        "command": 'apply_tile_mod',
        "args": [Rooms._306_SEASIDE_TOWN_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_158',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_159',
        "command": 'apply_tile_mod',
        "args": [Rooms._052_MUSHROOM_KINGDOM_INN_2F, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_160',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_apply_tile_mod_161',
        "command": 'apply_tile_mod',
        "args": [Rooms._346_NIMBUS_LAND_INN_BEDROOM, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_162',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_sync_163_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_action_queue_async_164',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_end_loop_9',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_shift_southwest_steps_21',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_shift_west_steps_22',
                "command": 'shift_west_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_face_northwest_23',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_164_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_set_action_script_sync_165',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 787],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_dialog_166',
        "command": 'run_dialog',
        "args": [3797, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_167',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_shift_west_steps_5',
                "command": 'shift_west_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_167_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_run_dialog_168',
        "command": 'run_dialog',
        "args": [3798, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_169',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_action_script_170',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_action_script_async_171',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_172',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_async_172_SUBSCRIPT_fixed_f_coord_off_11',
                "command": 'fixed_f_coord_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_pause_173',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_async_174',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_async_174_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_273_action_queue_async_174_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_run_dialog_175',
        "command": 'run_dialog',
        "args": [3799, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_176',
        "command": 'set',
        "args": [0x70a7, 107],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_177',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_event_as_subroutine_178',
        "command": 'run_event_as_subroutine',
        "args": [3827],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_put_inventory_179',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_run_dialog_180',
        "command": 'run_dialog',
        "args": [3796, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_pause_181',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_action_queue_sync_182',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_182_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_273_action_queue_sync_183',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_273_action_queue_sync_183_SUBSCRIPT_face_south_5',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_273_remember_last_object_184',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_action_script_sync_185',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_clear_bit_186',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_set_bit_187',
        "command": 'set_bit',
        "args": [0x7098, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_273_ret_188',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
