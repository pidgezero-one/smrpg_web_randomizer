from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3658_jmp_0',
        "command": 'jmp',
        "args": ['EVENT_3658_jmp_to_event_136']
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 45, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_4_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_4_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_5',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_fade_in_from_black_sync_6',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_sequence_looping_on_10',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_11_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_12',
        "command": 'pause',
        "args": [160]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_13_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_13_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 45, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_13_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_freeze_camera_14',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_face_north_3',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_face_east_7',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_15_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_16',
        "command": 'run_dialog',
        "args": [2528, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 811]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3658_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_21_SUBSCRIPT_set_solidity_bits_14',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_22',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_23',
        "command": 'run_dialog',
        "args": [2529, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x9e]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0050]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x9a]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x20, 0xb3, 0x9b]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_24_SUBSCRIPT_stop_sound_10',
                "command": 'stop_sound'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_26_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_26_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_27',
        "command": 'run_dialog',
        "args": [2530, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_28',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3658_jmp_if_object_in_air_29',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_12, 'EVENT_3658_pause_28']
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_31',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_run_dialog_32',
        "command": 'run_dialog',
        "args": [2531, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_unfreeze_camera_34',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [21]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_36_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_37',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_38',
        "command": 'run_dialog',
        "args": [2532, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_39',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_40',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_walk_1_step_north_5',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_shift_east_pixels_9',
                "command": 'shift_east_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_42_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_42_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_43',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_44_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_46_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_50_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_51',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_52',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_53_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_54_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_54_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_54_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_55_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_56',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_57',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_58',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3658_pause_59',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_60_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_60_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_60_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_60_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_60_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_61',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_62',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_palette_set_63',
        "command": 'palette_set',
        "args": [105, 1]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_64_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_65_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [5, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_66',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_pause_67',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_transfer_to_object_xy_1',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_69_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_70',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_71',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_72_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [10, 251, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_72_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_summon_to_current_level_73',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_74',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_fade_out_music_to_volume_75',
        "command": 'fade_out_music_to_volume',
        "args": [3, 1]
    },
    {
        "identifier": 'EVENT_3658_pause_76',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3658_play_sound_77',
        "command": 'play_sound',
        "args": [Sounds._006_RUNNING_WATER, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_78',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 113, 1]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_79',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 122, 2]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_80',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 123, 3]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_81',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 124, 4]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_82',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 125, 5]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_83',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 126, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_84',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 127, 7]
    },
    {
        "identifier": 'EVENT_3658_pause_85',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_86',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_87',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_88',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_89',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_90',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_91',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_92',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_93',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_94',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_95',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 376]
    },
    {
        "identifier": 'EVENT_3658_pause_short_96',
        "command": 'pause_short',
        "args": [270]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_97',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 114, 1]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_98',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 130, 2]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_99',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 131, 3]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_100',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 132, 4]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_101',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 133, 5]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_102',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 134, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_103',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 135, 7]
    },
    {
        "identifier": 'EVENT_3658_fade_out_sound_to_volume_104',
        "command": 'fade_out_sound_to_volume',
        "args": [3, 0]
    },
    {
        "identifier": 'EVENT_3658_fade_out_music_to_volume_105',
        "command": 'fade_out_music_to_volume',
        "args": [3, 127]
    },
    {
        "identifier": 'EVENT_3658_pause_106',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_107',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_108',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_109',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_110',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_111',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 626]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_113',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 627]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_114',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 625]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_115',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 627]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_116',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 811]
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_117',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_118_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [246, 5, 24, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_118_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_118_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_summon_to_current_level_119',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_pause_120',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_122_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_123',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_124',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_pause_125',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_freeze_camera_126',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_127',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [20, 36, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_127_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_128',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_129',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_129_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_129_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_129_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3658_action_queue_async_129_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_132_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_132_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_132_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_132_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_132_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_133',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_fade_out_to_black_sync_duration_134',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_pause_script_until_effect_done_135',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3658_jmp_to_event_136',
        "command": 'jmp_to_event',
        "args": [3738]
    }
]
