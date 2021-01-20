from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_329_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 3, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_run_dialog_5',
        "command": 'run_dialog',
        "args": [567, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_6_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_329_pause_7',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_freeze_camera_8',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_9_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [9, 87, 13]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_summon_to_current_level_10',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xd8]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_object_memory_clear_bit_7',
                "command": 'object_memory_clear_bit',
                "args": [0x09, [7]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_walk_1_step_southwest_11',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_db_15',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xed]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_floating_off_16',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_17',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_19',
                "command": 'shift_southeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_8',
                "command": 'transfer_to_xyzf',
                "args": [8, 106, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_13_SUBSCRIPT_floating_off_11',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_329_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_14_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_pause_15',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_play_sound_balance_16',
        "command": 'play_sound_balance',
        "args": [Sounds._068_MALLOW_YELLING_AT_CROCO, 64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_17_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_stop_sound_18',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_jump_to_height_silent_21',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_db_23',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1e, 0x6e]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_reset_properties_25',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_animation_speed_26',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_walk_1_step_southeast_27',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._069_MALLOW_FALLING_LANDING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_21',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_play_sound_balance_22',
        "command": 'play_sound_balance',
        "args": [Sounds._068_MALLOW_YELLING_AT_CROCO, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_23_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_remember_last_object_24',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_25',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_27',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_run_dialog_28',
        "command": 'run_dialog',
        "args": [567, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [17, 100, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xab]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_jump_to_height_silent_10',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_walk_1_step_northeast_12',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_db_14',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xb8]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_clear_solidity_bits_16',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_clear_solidity_bits_17',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_floating_off_18',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_shift_northwest_steps_19',
                "command": 'shift_northwest_steps',
                "args": [12]
            },
            {
                "identifier": 'EVENT_329_action_queue_sync_29_SUBSCRIPT_visibility_off_20',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_329_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_play_sound_balance_1',
                "command": 'play_sound_balance',
                "args": [Sounds._068_MALLOW_YELLING_AT_CROCO, 192]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [18]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [17, 100, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_shift_northwest_steps_12',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_stop_sound_13',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_face_northwest_16',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_face_northeast_18',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_end_loop_20',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_face_northeast_21',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_face_northwest_23',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_face_northeast_25',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_33',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_36',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_37',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_38',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_39',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_pause_40',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_41',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_jump_to_height_42',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_set_animation_speed_43',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_shift_northeast_pixels_44',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_30_SUBSCRIPT_floating_off_45',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_329_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._069_MALLOW_FALLING_LANDING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_32_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._070_MALLOW_SLIDING_ON_WALL, 6]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_pause_34',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_run_dialog_35',
        "command": 'run_dialog',
        "args": [572, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 76],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_37',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_run_dialog_38',
        "command": 'run_dialog',
        "args": [573, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_script_resume_on_next_dialog_page_a_39',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_unsync_dialog_41',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_42_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_329_action_queue_async_42_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_42_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 77],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_set_bit_44',
        "command": 'set_bit',
        "args": [0x7081, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_remove_from_current_level_45',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_46',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_47',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 17, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_48',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 18, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_49',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 19, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_50',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 20, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_51',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 21, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_52',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 22, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_palette_set_morphs_53',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 23, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_play_sound_54',
        "command": 'play_sound',
        "args": [Sounds._006_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_pause_55',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_run_event_as_subroutine_56',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_set_action_script_sync_57',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_329_action_queue_async_58_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x09, [7]]
            },
            {
                "identifier": 'EVENT_329_action_queue_async_58_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x09, [7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_329_set_action_script_sync_59',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_unfreeze_camera_60',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_329_ret_61',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
