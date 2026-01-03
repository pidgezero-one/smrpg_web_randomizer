
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3153_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 0, 'EVENT_3153_ret_85']
    },
    {
        "identifier": 'EVENT_3153_set_bit_1',
        "command": 'set_bit',
        "args": [0x7056, 0]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [26, 106]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_2_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_short_1',
                "command": 'set_short',
                "args": [0x701a, 0x0000]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_10',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_face_northwest_12',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_3_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 4, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_4_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [150]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [1, 4, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, 3, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_start_loop_n_times_14',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_jmp_if_bit_clear_17',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_16']
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_clear_bit_18',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_5_SUBSCRIPT_end_loop_21',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_pause_short_2',
                "command": 'pause_short',
                "args": [310]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_set_bit_6',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_sequence_playback_off_13',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_6_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_face_northwest_15',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_7_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [170]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_8_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [200]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_9_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_walk_1_step_northeast_10',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_face_northwest_14',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_sequence_playback_off_16',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_10_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_pause_short_2',
                "command": 'pause_short',
                "args": [400]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_set_bit_9',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_shift_southeast_steps_12',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_face_northwest_13',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_11_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [220]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_12_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_12_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_12_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_13_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_13_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_13_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [95]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_14_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_pause_short_0',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_sequence_playback_off_9',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_15_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [280]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_sequence_playback_on_6',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7043, 0]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_shift_southwest_steps_12',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_13',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_face_northwest_14',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_16_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [110]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_shift_west_pixels_8',
                "command": 'shift_west_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_17_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [160]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_18_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_18_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_18_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_18_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [180]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_19_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_19_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [200]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_sequence_playback_off_9',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_20_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [21, 77]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_22',
        "command": 'run_dialog',
        "args": [1600, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_23_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_23_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_23_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_24',
        "command": 'run_dialog',
        "args": [1601, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_26_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_26_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_2',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._027_TERRAPIN, AreaObjects.NPC_6, 'EVENT_3153_action_queue_async_27_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._101_TERRAPIN_ATTACK, 4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_jmp_if_bit_clear_7',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3153_action_queue_async_27_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_walk_1_step_southeast_9',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_27_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_28',
        "command": 'run_dialog',
        "args": [1602, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_1',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._026_MAGIKOOPA_SFX, AreaObjects.NPC_11, 'EVENT_3153_action_queue_async_31_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_jmp_if_bit_clear_5',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3153_action_queue_async_31_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_walk_1_step_southeast_7',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_31_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_32',
        "command": 'run_dialog',
        "args": [1603, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_33_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_34_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_34_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_34_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_34_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._045_GOOMBA_TAUNT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_tint_layers_35',
        "command": 'tint_layers',
        "args": [0xa0, 0x20, 0x20, 5, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_4, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_3153_pause_36',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3153_tint_layers_37',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 5, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_4, _0x81Flags.BACKGROUND], []]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_38_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_38_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_38_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_38_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_reset_priority_set_39',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_3153_run_dialog_40',
        "command": 'run_dialog',
        "args": [1604, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_41_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_41_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_41_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_42_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_42_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_42_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_43',
        "command": 'run_dialog',
        "args": [1605, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._057_FINGER_SNAP, 4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_set_priority_10',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_44_SUBSCRIPT_visibility_off_12',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._046_CRUMBLING_NOISE, 4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_45_SUBSCRIPT_ret_9',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_46_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_47_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_48_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_49_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [250]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_50_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [250]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_51_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [250]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_52_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [250]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_53_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [250]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_54_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_55_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_56_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_57_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_58_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_59_SUBSCRIPT_ret_8',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_60_SUBSCRIPT_pause_short_0',
                "command": 'pause_short',
                "args": [380]
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_60_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_fade_out_sound_to_volume_61',
        "command": 'fade_out_sound_to_volume',
        "args": [8, 0]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 5, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_62_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7043, 1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_sync_63_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3153_action_queue_sync_63_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_run_dialog_64',
        "command": 'run_dialog',
        "args": [1606, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3153_pause_65',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3153_jmp_if_bit_clear_66',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3153_pause_65']
    },
    {
        "identifier": 'EVENT_3153_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3153_action_queue_async_67_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_67_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_67_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3153_action_queue_async_67_SUBSCRIPT_object_memory_set_bit_3',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_68',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_69',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_70',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_71',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_72',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_73',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_74',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_75',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_76',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_77',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_78',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_79',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_80',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_12, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_81',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_82',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_14, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_83',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_15, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_remove_from_level_84',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_3153_ret_85',
        "command": 'ret'
    }
]
