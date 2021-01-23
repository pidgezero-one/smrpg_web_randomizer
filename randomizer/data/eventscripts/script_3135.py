from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3135_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_3135_set_short_1',
        "command": 'set_short',
        "args": [0x701c, 0x012c]
    },
    {
        "identifier": 'EVENT_3135_stop_background_event_2',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3135_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70df, 14, 'EVENT_3135_jmp_if_bit_set_7']
    },
    {
        "identifier": 'EVENT_3135_jmp_to_subroutine_4',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3134_summon_to_level_15']
    },
    {
        "identifier": 'EVENT_3135_set_5',
        "command": 'set',
        "args": [0x70df, 14]
    },
    {
        "identifier": 'EVENT_3135_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_3135_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_3135_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3135_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_3135_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3134_summon_to_level_15']
    },
    {
        "identifier": 'EVENT_3135_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7055, 1, 'EVENT_3135_reset_priority_set_14']
    },
    {
        "identifier": 'EVENT_3135_set_7000_to_current_level_10',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3135_jmp_if_7000_equals_short_11',
        "command": 'jmp_if_7000_equals_short',
        "args": [62, 'EVENT_3135_run_event_as_subroutine_15']
    },
    {
        "identifier": 'EVENT_3135_priority_set_12',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [], []]
    },
    {
        "identifier": 'EVENT_3135_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_3135_run_event_as_subroutine_15']
    },
    {
        "identifier": 'EVENT_3135_reset_priority_set_14',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_3135_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3135_set_7000_to_current_level_16',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3135_jmp_if_7000_not_equals_short_17',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [333, 'EVENT_3135_ret_32']
    },
    {
        "identifier": 'EVENT_3135_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 0, 'EVENT_3135_ret_32']
    },
    {
        "identifier": 'EVENT_3135_set_bit_19',
        "command": 'set_bit',
        "args": [0x7055, 0]
    },
    {
        "identifier": 'EVENT_3135_enable_controls_until_return_20',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.A, ControllerDirections.Y]]
    },
    {
        "identifier": 'EVENT_3135_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3135_action_queue_async_21_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3135_action_queue_async_21_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_3135_summon_to_current_level_at_marios_coords_22',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3135_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_set_bit_6',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_jmp_if_bit_clear_8',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_jump_to_height_silent_12',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_walk_1_step_northwest_13',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_db_15',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x48, 0x11]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [20, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_play_sound_18',
                "command": 'play_sound',
                "args": [Sounds._028_PIPE_ENTRANCE, 6]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [30, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_clear_solidity_bits_20',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_dec_z_coord_1_step_21',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_23_SUBSCRIPT_visibility_off_22',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3135_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_walk_1_step_northeast_6',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_face_south_7',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3135_action_queue_sync_24_SUBSCRIPT_set_bit_9',
                "command": 'set_bit',
                "args": [0x7043, 3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3135_pause_25',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3135_jmp_if_bit_clear_26',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3135_pause_25']
    },
    {
        "identifier": 'EVENT_3135_run_dialog_27',
        "command": 'run_dialog',
        "args": [1584, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3135_set_bit_28',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3135_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3135_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3135_pause_29']
    },
    {
        "identifier": 'EVENT_3135_pause_31',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3135_ret_32',
        "command": 'ret'
    }
]
