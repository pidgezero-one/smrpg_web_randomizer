from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_622_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 12, 'EVENT_622_run_dialog_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_622_run_dialog_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_run_dialog_3',
        "command": 'run_dialog',
        "args": [1018, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_4',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [6, 62]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_5_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_6_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_6_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_6_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_7_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_7_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_pause_8',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_remember_last_object_11',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_12_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_12_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_12_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_12_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_13_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_13_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_14_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_14_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_pause_15',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_fade_out_to_black_async_16',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._006_MARRYMORE_INN_2F, RadialDirections.NORTHEAST, 15, 52, 1, [_0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_fade_in_from_black_sync_18',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [15, 52, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_start_loop_n_times_14',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_shift_southeast_pixels_15',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_shift_northwest_pixels_16',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_end_loop_18',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_fixed_f_coord_off_19',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_20_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [74]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [46]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [15, 52, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_walk_1_step_northwest_8',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [74]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_shift_northwest_pixels_14',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_shift_southeast_pixels_15',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_face_northwest_18',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_off_19',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_21_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_remember_last_object_22',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_23_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_23_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_23_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_24_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_25_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_pause_26',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_fade_out_to_black_async_27',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_enter_area_28',
        "command": 'enter_area',
        "args": [Rooms._011_MARRYMORE_INN_3F, RadialDirections.NORTHEAST, 12, 73, 1, [_0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_fade_in_from_black_sync_29',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_clear_solidity_bits_9',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_30_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [12, 73, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_31_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [46]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [12, 73, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_32_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_pause_33',
        "command": 'pause',
        "args": [52],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_apply_tile_mod_35',
        "command": 'apply_tile_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_apply_solidity_mod_36',
        "command": 'apply_solidity_mod',
        "args": [Rooms._011_MARRYMORE_INN_3F, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_37',
        "command": 'pause',
        "args": [70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_38_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_fade_out_to_black_async_39',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_enter_area_40',
        "command": 'enter_area',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, RadialDirections.NORTHEAST, 3, 21, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_set_bit_41',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_async_42_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_fade_in_from_black_sync_43',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_44_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_44_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_45_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_45_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_45_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_45_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_walk_1_step_east_6',
                "command": 'walk_1_step_east',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_46_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_remember_last_object_47',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_freeze_camera_48',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_49',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_50',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_set_action_script_async_51',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_52_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_52_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_52_SUBSCRIPT_face_south_3',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_53_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_53_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_54_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_remember_last_object_55',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_56',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_set_action_script_async_57',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_58',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_set_action_script_async_59',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_60_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_60_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_61_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_sync_62_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_sync_62_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_remember_last_object_63',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_64',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_play_sound_65',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_66',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_async_67_SUBSCRIPT_shift_west_steps_0',
                "command": 'shift_west_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_67_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_622_action_queue_async_67_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_622_set_action_script_async_68',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_pause_69',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_622_action_queue_async_70_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_622_set_bit_71',
        "command": 'set_bit',
        "args": [0x704c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_unfreeze_camera_72',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_ret_73',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_run_dialog_74',
        "command": 'run_dialog',
        "args": [2050, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_ret_75',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_run_dialog_76',
        "command": 'run_dialog',
        "args": [2052, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_622_ret_77',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
