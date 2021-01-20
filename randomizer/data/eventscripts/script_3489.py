from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3489_set_short_0',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 0, 'EVENT_3489_enable_controls_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_2',
        "command": 'set',
        "args": [0x70d4, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_3',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_4',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_run_background_event_5',
        "command": 'run_background_event',
        "args": [3490, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_run_background_event_6',
        "command": 'run_background_event',
        "args": [3481, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_move_script_to_background_thread_2_7',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3489_fade_out_to_black_async_duration_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_9',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_7000_to_tapped_button_11',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3489_enable_controls_until_return_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_13',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_pause_14',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_7000_to_tapped_button_15',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_16',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3489_enable_controls_until_return_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_7000_to_pressed_button_17',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_18',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_3489_action_queue_sync_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_19',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_3489_action_queue_sync_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3489_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_sync_21_SUBSCRIPT_face_west_0',
                "command": 'face_west',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3489_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_sync_23_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_3489_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_25',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_pause_action_script_26',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_set_short_28',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_29',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_async_30_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_3489_action_queue_async_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3489_action_queue_async_30_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3489_action_queue_async_30_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_add_short_31',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_var_equals_short_32',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 5, 'EVENT_3489_enable_controls_until_return_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_temp_action_script_sync_34',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 465],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_35',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_pause_36',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_7000_to_tapped_button_37',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_38',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3489_enable_controls_until_return_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_39',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_pause_40',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_7000_to_tapped_button_41',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_if_7000_any_bits_set_42',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_3489_enable_controls_until_return_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_end_loop_43',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_until_return_44',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_set_object_memory_to_45',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_sync_46_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3489_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3489_action_queue_async_47_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3489_action_queue_async_47_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3489_end_loop_48',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_resume_action_script_49',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_3489_jmp_if_bit_set_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_fade_out_to_black_async_duration_51',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enable_controls_53',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_enter_area_54',
        "command": 'enter_area',
        "args": [Rooms._068_MIDAS_RIVER_BARREL_JUMPING_RIVER, RadialDirections.SOUTHWEST, 13, 16, 3, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3489_ret_55',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
