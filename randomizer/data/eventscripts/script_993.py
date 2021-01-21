from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_993_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._245_GAME_INTRO_PIPE_VAULT_AREA_02_WTHWOMP, RadialDirections.NORTHEAST, 22, 33, 1, []]
    },
    {
        "identifier": 'EVENT_993_run_background_event_1',
        "command": 'run_background_event',
        "args": [429, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_993_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_993_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_2_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_2_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_993_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jmp_if_mario_in_air_12',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_11']
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_13',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_14',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_15',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jmp_if_mario_in_air_17',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_16']
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_walk_1_step_northeast_19',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_20',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_22',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_23',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jmp_if_mario_in_air_25',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_993_action_queue_sync_3_SUBSCRIPT_pause_24']
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_26',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_shift_northeast_steps_28',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_floating_off_29',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_993_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_shift_z_down_steps_4',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_bit_5',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_clear_bit_9',
                "command": 'clear_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_4_SUBSCRIPT_shift_z_up_steps_13',
                "command": 'shift_z_up_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_993_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_993_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_5_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_993_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_add_z_coord_1_step_5',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_993_action_queue_sync_6_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_993_pause_7',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_993_fade_in_from_black_sync_8',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_993_pause_9',
        "command": 'pause',
        "args": [98]
    },
    {
        "identifier": 'EVENT_993_fade_out_to_black_sync_duration_10',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_993_pause_script_until_effect_done_11',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_993_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [138]
    }
]
