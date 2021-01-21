from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3203_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 4, 'EVENT_3203_ret_33']
    },
    {
        "identifier": 'EVENT_3203_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 2, 'EVENT_3203_ret_33']
    },
    {
        "identifier": 'EVENT_3203_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_3_SUBSCRIPT_face_mario_0',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_3_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_3_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_4_SUBSCRIPT_face_mario_0',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_5_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [4, 24]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_5_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_5_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_5_SUBSCRIPT_sequence_playback_on_4',
                "command": 'sequence_playback_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_6_SUBSCRIPT_face_mario_0',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_7_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [1, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_8_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_run_dialog_9',
        "command": 'run_dialog',
        "args": [1643, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 4, 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_10_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_walk_1_step_northwest_7',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_set_bit_9',
                "command": 'set_bit',
                "args": [0x7043, 4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_on_10',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_shift_southeast_steps_11',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_off_12',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_11_SUBSCRIPT_face_northwest_13',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_12_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_13_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_14_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_pause_short_15',
        "command": 'pause_short',
        "args": [360]
    },
    {
        "identifier": 'EVENT_3203_store_02_to_0248_16',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_3203_set_bit_17',
        "command": 'set_bit',
        "args": [0x707c, 4]
    },
    {
        "identifier": 'EVENT_3203_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3203_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3203_apply_solidity_mod_20',
        "command": 'apply_solidity_mod',
        "args": [Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3203_pause_21',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3203_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x707c, 4]
    },
    {
        "identifier": 'EVENT_3203_store_00_to_0248_23',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_3203_pause_24',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3203_jmp_if_bit_clear_25',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_3203_pause_24']
    },
    {
        "identifier": 'EVENT_3203_set_bit_26',
        "command": 'set_bit',
        "args": [0x7057, 2]
    },
    {
        "identifier": 'EVENT_3203_pause_27',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_28_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 19, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_bounce_to_xy_with_height_6',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 18, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_29_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 19, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_bounce_to_xy_with_height_6',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 18, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_sync_30_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 19, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_bounce_to_xy_with_height_6',
                "command": 'bounce_to_xy_with_height',
                "args": [3, 18, 0]
            },
            {
                "identifier": 'EVENT_3203_action_queue_async_31_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3203_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3203_ret_33',
        "command": 'ret'
    }
]
