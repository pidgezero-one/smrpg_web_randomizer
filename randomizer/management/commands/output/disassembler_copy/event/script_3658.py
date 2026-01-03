
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3658_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_0_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 45, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_2_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_3_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_4',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_fade_in_from_black_sync_5',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_6_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_7_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_8_SUBSCRIPT_sequence_looping_on_10',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_9_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [7]
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
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_10_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_11',
        "command": 'pause',
        "args": [160]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_12_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 45, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_12_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_freeze_camera_13',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_face_north_3',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_face_east_7',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_14_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_15',
        "command": 'run_dialog',
        "args": [2528, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 811]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3658_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_20_SUBSCRIPT_set_solidity_bits_14',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_21',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_22',
        "command": 'run_dialog',
        "args": [2529, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x9e]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x701a, 0x0050]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x9a]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x20, 0xb3, 0x9b]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_23_SUBSCRIPT_stop_sound_10',
                "command": 'stop_sound'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_26',
        "command": 'run_dialog',
        "args": [2530, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3658_jmp_if_object_in_air_28',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_12, 'EVENT_3658_pause_27']
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_30',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_run_dialog_31',
        "command": 'run_dialog',
        "args": [2531, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_unfreeze_camera_33',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_34_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_34_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_34_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [21]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_35_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_36',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_run_dialog_37',
        "command": 'run_dialog',
        "args": [2532, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3658_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_39',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_walk_1_step_north_5',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_shift_east_pixels_9',
                "command": 'shift_east_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_41_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_42',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_43_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_44',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_45_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_49_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_50',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_51',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_53_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_53_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_53_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_54_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_55',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_57',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3658_pause_58',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_59_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_59_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_59_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_59_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_60',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_pause_61',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_palette_set_62',
        "command": 'palette_set',
        "args": [105, 1, [1, 2, 3]]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_63_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_63_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [5, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_65',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_pause_66',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_transfer_to_object_xy_1',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_68_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_69',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_70',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_71_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [10, 251, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_71_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_71_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_summon_to_current_level_72',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_73',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_fade_out_music_to_volume_74',
        "command": 'fade_out_music_to_volume',
        "args": [3, 1]
    },
    {
        "identifier": 'EVENT_3658_pause_75',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3658_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._006_RUNNING_WATER, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_77',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 113, 1]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_78',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 122, 2]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_79',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 123, 3]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_80',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 124, 4]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_81',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 125, 5]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_82',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 126, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_83',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 127, 7]
    },
    {
        "identifier": 'EVENT_3658_pause_84',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_85',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_86',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_87',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_88',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_89',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_90',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_91',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_92',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_93',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 376]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_94',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 376]
    },
    {
        "identifier": 'EVENT_3658_pause_short_95',
        "command": 'pause_short',
        "args": [270]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_96',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 114, 1]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_97',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 130, 2]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_98',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 131, 3]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_99',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 132, 4]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_100',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 133, 5]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_101',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 134, 6]
    },
    {
        "identifier": 'EVENT_3658_palette_set_morphs_102',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 135, 7]
    },
    {
        "identifier": 'EVENT_3658_fade_out_sound_to_volume_103',
        "command": 'fade_out_sound_to_volume',
        "args": [3, 0]
    },
    {
        "identifier": 'EVENT_3658_fade_out_music_to_volume_104',
        "command": 'fade_out_music_to_volume',
        "args": [3, 127]
    },
    {
        "identifier": 'EVENT_3658_pause_105',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_106',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_107',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_108',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_109',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3658_pause_action_script_110',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_111',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 626]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 627]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_113',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 625]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_async_114',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 627]
    },
    {
        "identifier": 'EVENT_3658_set_action_script_sync_115',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 811]
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_116',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_117',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_117_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [246, 5, 24, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_117_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_117_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_summon_to_current_level_118',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_pause_119',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_120_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_120_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 5, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_120_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_120_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_121_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_remember_last_object_122',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3658_remove_from_current_level_123',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3658_pause_124',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3658_freeze_camera_125',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [20, 36, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_126_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_127',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_action_queue_async_128',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_async_128_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_128_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3658_action_queue_async_128_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3658_action_queue_async_128_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_129_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_129_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_129_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_129_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_130_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3658_action_queue_sync_131_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3658_pause_132',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3658_fade_out_to_black_sync_duration_133',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3658_pause_script_until_effect_done_134',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3658_jmp_to_event_135',
        "command": 'jmp_to_event',
        "args": [3738]
    }
]
