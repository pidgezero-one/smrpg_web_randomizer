from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_0',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_2',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_9',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_10',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_13_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 41, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_14_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_14_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_14_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_16',
        "command": 'set',
        "args": [0x70a9, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_18',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_19',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_20',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_26',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_27',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_28',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_30',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_31_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_31_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_31_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_32_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 39, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_32_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_32_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_34',
        "command": 'set',
        "args": [0x70a9, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_36',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_37',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_38',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_39',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_41',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_43',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_44',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_45',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_47',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_49_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_49_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_50_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [9, 37, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_50_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_50_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_50_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_52',
        "command": 'set',
        "args": [0x70a9, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_53',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_54',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_55',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_56',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_57',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_59',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_62',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_63',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_64',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x7012, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_66',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_67_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_67_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_67_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_68_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 35, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_68_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_68_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_68_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_69',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_70',
        "command": 'set',
        "args": [0x70a9, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_71',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_72',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_73',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_74',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_75',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_77'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_76',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_77',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_78',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_79',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_80',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_81',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_82',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_83',
        "command": 'set_short_mem',
        "args": [0x7012, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_84',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_85_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_85_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_85_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_86_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 33, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_86_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_86_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_86_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_87',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_88',
        "command": 'set',
        "args": [0x70a9, 25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_90',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_91',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_92',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_93',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_95'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_94',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_90'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_95',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_90'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_96',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_97',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_98',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_99',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_100',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_101',
        "command": 'set_short_mem',
        "args": [0x7012, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_102',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_103_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_103_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_103_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_104_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 31, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_104_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_104_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_104_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_105',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_106',
        "command": 'set',
        "args": [0x70a9, 26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_107',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_108',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_109',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_110',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_111',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_113'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_112',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_108'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_113',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_108'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_114',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_115',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_116',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_117',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_118',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_119',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_120',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_sync_121_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_121_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1073_action_queue_sync_121_SUBSCRIPT_ret_2',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_122',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_122_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 29, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_122_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_122_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_122_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_123',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 570],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_124',
        "command": 'set',
        "args": [0x70a9, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_125',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 515],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_7000_to_tapped_button_126',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_127',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_mem_7000_and_const_128',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_129',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1073_jmp_if_bit_clear_131'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_130',
        "command": 'jmp',
        "args": ['EVENT_1073_set_7000_to_tapped_button_126'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_bit_clear_131',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1073_set_7000_to_tapped_button_126'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_action_script_sync_132',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 571],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_133',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_134',
        "command": 'jmp_to_subroutine',
        "args": [0xb955],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_135',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_136',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_137',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_138',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7032],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_139',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_140',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_141',
        "command": 'set_short',
        "args": [0x7012, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_set_short_mem_142',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7012],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_dec_short_mem_143',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_to_subroutine_144',
        "command": 'jmp_to_subroutine',
        "args": [0xb2f4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_145',
        "command": 'jmp',
        "args": ['EVENT_1074_set_bit_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_ret_146',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_147',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1073_pause_action_script_160'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_148',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1073_pause_action_script_163'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_149',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_1073_pause_action_script_166'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_150',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_1073_pause_action_script_169'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_151',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_1073_pause_action_script_172'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_152',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_1073_pause_action_script_175'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_153',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1073_pause_action_script_178'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_154',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65535, 'EVENT_1073_pause_action_script_181'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_155',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65534, 'EVENT_1073_pause_action_script_184'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_156',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65533, 'EVENT_1073_pause_action_script_187'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_157',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65532, 'EVENT_1073_pause_action_script_190'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_158',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65531, 'EVENT_1073_pause_action_script_193'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_jmp_if_var_equals_short_159',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65530, 'EVENT_1073_pause_action_script_196'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_160',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_161',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x02, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_161_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_162',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_163',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_164',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x01, 0x80, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_164_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_165',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_166',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_167',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_face_north_0',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x00, 0xab, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_167_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_168',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_169',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_170',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_face_north_0',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x56, 0xff, 0x56, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_170_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_171',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_172',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_173',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0xab, 0xfe, 0x00, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_173_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_174',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_175',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_176',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x80, 0xfe, 0x40, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_176_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_177',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_178',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_179',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0xfe, 0x00, 0xfe]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_179_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_180',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_181',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_182',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x02, 0xab, 0xff]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_182_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_183',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_184',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_185',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0xaa, 0x02, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_185_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_186',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_187',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_188',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x55, 0x03, 0x55, 0x00]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_188_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_189',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_190',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_191',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x04, 0xaa, 0x00]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_191_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_192',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_193',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_194',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x80, 0x03, 0xc0, 0x00]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_194_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_195',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_pause_action_script_196',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1073_action_queue_async_197',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x04, 0x00, 0x01]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1073_action_queue_async_197_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1073_ret_198',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
