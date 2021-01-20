from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3491_fade_in_from_black_sync_0',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 598],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3491_action_queue_sync_3_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3491_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_jmp_to_subroutine_4',
        "command": 'jmp_to_subroutine',
        "args": [0x6752],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 8, 31, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_fade_out_music_to_volume_6',
        "command": 'fade_out_music_to_volume',
        "args": [1, 56],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_async_8_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 29]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_10_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x7016, 0x1980]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_10_SUBSCRIPT_set_short_3',
                "command": 'set_short',
                "args": [0x7018, 0x0e80]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_10_SUBSCRIPT_run_away_transfer_4',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": [0x6247],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x80, 0x02, 0xf4, 0xff]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_walk_1_step_southwest_8',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3491_action_queue_async_12_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 466],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3489_enable_controls_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_21',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_23',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_24',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_27',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_29',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_30',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_33',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_35',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_36',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_37',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_39',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_41',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_42',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_45',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_47',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_48',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_50',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_51',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_53',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_54',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_55',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_56',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_57',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3491_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3491_start_loop_n_times_59',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_pause_60',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_61',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3491_fade_out_to_black_async_duration_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_if_bit_set_62',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 5, 'EVENT_3491_start_loop_n_times_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_end_loop_63',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_3491_action_queue_sync_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_fade_out_to_black_async_duration_65',
        "command": 'fade_out_to_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3491_ret_66',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
