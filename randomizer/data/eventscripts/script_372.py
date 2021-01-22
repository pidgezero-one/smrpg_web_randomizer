from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_372_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_372_set_bit_1',
        "command": 'set_bit',
        "args": [0x7082, 4]
    },
    {
        "identifier": 'EVENT_372_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_372_action_queue_async_3_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [15, 31, 4]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_async_3_SUBSCRIPT_floating_on_9',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_remember_last_object_4',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_372_pause_5',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_372_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 103]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_8_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_run_dialog_9',
        "command": 'run_dialog',
        "args": [623, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_372_remember_last_object_10',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_372_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_372_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 103]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_15_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_run_dialog_16',
        "command": 'run_dialog',
        "args": [624, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_372_remember_last_object_17',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_372_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_pause_19',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_372_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x07, 0x70, 0xff]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [15]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 6]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_13',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_floating_on_14',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_walk_1_step_northwest_15',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_shift_northwest_pixels_16',
                "command": 'shift_northwest_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_db_18',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0x7f, 0x2a]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_19',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_walk_1_step_northwest_20',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_db_22',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0x8a, 0x2a]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_23',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_21_SUBSCRIPT_floating_off_24',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x07, 0x70, 0xff]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [15]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_floating_on_12',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_walk_1_step_southeast_13',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_shift_southeast_pixels_14',
                "command": 'shift_southeast_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_db_16',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xb6, 0x2a]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_jump_to_height_silent_17',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_walk_1_step_southeast_18',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_db_20',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0xc1, 0x2a]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_clear_solidity_bits_21',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_22_SUBSCRIPT_floating_off_22',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_23_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [16, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_372_action_queue_sync_23_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_remember_last_object_24',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_25_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_26_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_27_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_sync_28_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_remember_last_object_29',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_372_pause_30',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 102]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 101]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 102]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 101]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 102]
    },
    {
        "identifier": 'EVENT_372_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 101]
    },
    {
        "identifier": 'EVENT_372_pause_37',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_372_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_372_action_queue_async_38_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_372_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_373_action_queue_sync_6']
    }
]
