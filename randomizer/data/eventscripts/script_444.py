from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_444_set_short_mem_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_444_close_dialog_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_close_dialog_2',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_3',
        "command": 'run_dialog',
        "args": [2541, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_dialog_option_b_4',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_444_set_action_script_async_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_7',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_8',
        "command": 'set',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [274],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_444_run_dialog_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_dec_coins_13',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 7, 'EVENT_444_run_dialog_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_15',
        "command": 'set',
        "args": [0x7000, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x70ec, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_17',
        "command": 'run_dialog',
        "args": [2542, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_dialog_option_b_18',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_444_set_action_script_async_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_20',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_close_dialog_21',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_22',
        "command": 'run_dialog',
        "args": [836, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_floating_off_2',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [4, 115]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_444_action_queue_async_23_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_444_run_dialog_24',
        "command": 'run_dialog',
        "args": [822, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_enable_controls_until_return_25',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_fade_out_music_to_volume_26',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_bit_27',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_to_event_28',
        "command": 'jmp_to_event',
        "args": [445],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_30',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ec],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_32',
        "command": 'run_dialog',
        "args": [2543, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_dialog_option_b_33',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_444_set_action_script_async_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_34',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_35',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_444_close_dialog_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_37',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_38',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_444_set_short_mem_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_pause_41',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_42',
        "command": 'run_dialog',
        "args": [839, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ec],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x703a, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_mem_compare_47',
        "command": 'mem_compare',
        "args": [0x7000, 0x703a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_comparison_result_is_greater_or_equal_48',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_444_set_short_mem_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_49',
        "command": 'run_dialog',
        "args": [840, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_enable_controls_50',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_clear_bit_51',
        "command": 'clear_bit',
        "args": [0x7049, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_clear_bit_52',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_ret_53',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_54',
        "command": 'run_dialog',
        "args": [879, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_ret_55',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_add_57',
        "command": 'add',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x70ec, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_59',
        "command": 'run_dialog',
        "args": [837, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_60',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 4, 'EVENT_444_jmp_if_bit_set_66'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_bit_61',
        "command": 'set_bit',
        "args": [0x7099, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_62',
        "command": 'set',
        "args": [0x70a7, 115],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_63',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_event_as_subroutine_64',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_444_enable_controls_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_if_bit_set_66',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 5, 'EVENT_444_play_sound_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_bit_67',
        "command": 'set_bit',
        "args": [0x7099, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_68',
        "command": 'set',
        "args": [0x70a7, 116],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_set_69',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_event_as_subroutine_70',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_71',
        "command": 'jmp',
        "args": ['EVENT_444_enable_controls_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_play_sound_72',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_73',
        "command": 'run_dialog',
        "args": [526, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_add_frog_coins_74',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_444_enable_controls_50'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_close_dialog_76',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_run_dialog_77',
        "command": 'run_dialog',
        "args": [838, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_444_ret_78',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
