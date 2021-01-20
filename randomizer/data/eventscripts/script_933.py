from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_933_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._130_BIG_BABY_YOSHI, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_932_enable_controls_until_return_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_store_item_amount_7000_3',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_6',
        "command": 'run_dialog',
        "args": [2364, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_7',
        "command": 'run_dialog',
        "args": [2372, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_dialog_option_b_8',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_9',
        "command": 'run_dialog',
        "args": [2373, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_bit_10',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": [0xa958],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_object_memory_to_16',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_remove_one_from_inventory_17',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_end_loop_18',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_add_short_mem_20',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_mem_compare_21',
        "command": 'mem_compare',
        "args": [0x7000, 50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_comparison_result_is_greater_or_equal_22',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_933_action_queue_async_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x70d9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_mem_compare_25',
        "command": 'mem_compare',
        "args": [0x7000, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_comparison_result_is_greater_or_equal_26',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_933_action_queue_async_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_mem_compare_27',
        "command": 'mem_compare',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_comparison_result_is_greater_or_equal_28',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_933_action_queue_async_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_29',
        "command": 'run_dialog',
        "args": [2375, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_31_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_31_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_33',
        "command": 'run_dialog',
        "args": [2374, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_34',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_to_subroutine_35',
        "command": 'jmp_to_subroutine',
        "args": [0xad25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_36',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_play_sound_37',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_38',
        "command": 'set',
        "args": [0x70a7, 107],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_39',
        "command": 'run_dialog',
        "args": [524, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_put_inventory_40',
        "command": 'put_inventory',
        "args": [items.RedEssence],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_42_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_42_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_pause_43',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_44',
        "command": 'run_dialog',
        "args": [2374, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_45',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0xad25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_47',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_random_49',
        "command": 'set_random',
        "args": [0x7000, 101],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_var_equals_short_50',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 100, 'EVENT_933_set_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_if_random_above_66_51',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_933_set_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_52',
        "command": 'set',
        "args": [0x70a7, 106],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_53',
        "command": 'run_dialog',
        "args": [524, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_put_inventory_54',
        "command": 'put_inventory',
        "args": [items.YoshiAde],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_55',
        "command": 'jmp',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_56',
        "command": 'set',
        "args": [0x70a7, 105],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_57',
        "command": 'run_dialog',
        "args": [524, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_put_inventory_58',
        "command": 'put_inventory',
        "args": [items.Energizer],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_60',
        "command": 'set',
        "args": [0x70a7, 104],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_61',
        "command": 'run_dialog',
        "args": [524, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_put_inventory_62',
        "command": 'put_inventory',
        "args": [items.Bracer],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_63',
        "command": 'jmp',
        "args": ['EVENT_933_close_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_64_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_64_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_pause_65',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_66',
        "command": 'run_dialog',
        "args": [2374, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_67',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_jmp_to_subroutine_68',
        "command": 'jmp_to_subroutine',
        "args": [0xad25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_pause_69',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_add_frog_coins_70',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_play_sound_71',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_dialog_72',
        "command": 'run_dialog',
        "args": [526, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_set_73',
        "command": 'set',
        "args": [0x70d9, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_close_dialog_74',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_run_background_event_75',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_clear_bit_80',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_ret_81',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_933_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_82_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_933_action_queue_async_82_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_83_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_83_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [110]
            },
            {
                "identifier": 'EVENT_933_action_queue_async_83_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_933_action_queue_async_84_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_933_action_queue_async_84_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_933_ret_85',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]