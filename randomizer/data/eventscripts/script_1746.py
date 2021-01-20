from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1746_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._149_GAME_INTRO_MIDAS_RIVER_BARREL_JUMPING, RadialDirections.SOUTHWEST, 13, 16, 3, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_2',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_3',
        "command": 'set_short',
        "args": [0x7026, 0x0016],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_4',
        "command": 'set_short',
        "args": [0x7028, 0x0015],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_run_background_event_5',
        "command": 'run_background_event',
        "args": [1585, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_6_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_freeze_camera_7',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_7016_to_object_xyz_8',
        "command": 'set_7016_to_object_xyz',
        "args": [0x95],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 170],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_10_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_10_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_async_11_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_fade_in_from_black_sync_12',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [13, 16, 17, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_13_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_14_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_15_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_floating_on_8',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1746_action_queue_async_16_SUBSCRIPT_shadow_off_9',
                "command": 'shadow_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 593],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 593],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 592],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_move_script_to_background_thread_2_20',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_21',
        "command": 'set_short',
        "args": [0x701c, 0x012c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_run_background_event_with_pause_return_on_exit_22',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1747, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_23',
        "command": 'set_short',
        "args": [0x701e, 0x008c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_run_background_event_with_pause_return_on_exit_24',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1749, 0x701e, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1746_clear_bit_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1746_set_short_mem_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_1746_pause_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_pause_action_script_30',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_pause_action_script_31',
        "command": 'pause_action_script',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_34_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_34_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_34_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_34_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_34_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_pause_action_script_35',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_36_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_36_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_resume_action_script_37',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_store_set_bits_38',
        "command": 'store_set_bits',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_pause_39',
        "command": 'pause',
        "args": [19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_resume_action_script_40',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_pause_41',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1746_action_queue_sync_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1746_action_queue_sync_42_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1746_add_short_43',
        "command": 'add_short',
        "args": [0x702c, 0xfff6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_1746_pause_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_action_script_sync_47',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 592],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 592],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_fade_out_to_black_async_duration_49',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1746_jmp_to_event_50',
        "command": 'jmp_to_event',
        "args": [1729],
        "subscript": []
    },
]
