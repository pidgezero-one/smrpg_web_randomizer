from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1702_jmp_if_object_trigger_disabled_0',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_9, Rooms._207_BANDITS_WAY_AREA_02, 'EVENT_1702_action_queue_async_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_1_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_async_2_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_3_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_4_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_4_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_5_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_6_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_jmp_if_bit_set_4',
                "command": 'jmp_if_bit_set',
                "args": [0x7077, 5, 'EVENT_1702_action_queue_async_8']
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_7_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_jmp_if_bit_set_4',
                "command": 'jmp_if_bit_set',
                "args": [0x7077, 6, 'EVENT_1702_set_action_script_sync_9']
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_8_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 477],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_set_short_10',
        "command": 'set_short',
        "args": [0x7024, 0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_set_short_11',
        "command": 'set_short',
        "args": [0x703e, 0x001a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7077, 1, 'EVENT_1702_set_bit_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_run_event_as_subroutine_14',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_1702_clear_bit_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_jmp_if_object_trigger_disabled_16',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_9, Rooms._207_BANDITS_WAY_AREA_02, 'EVENT_1702_clear_bit_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_set_bit_20',
        "command": 'set_bit',
        "args": [0x7077, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_fade_in_from_black_sync_21',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_22_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_pause_23',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_24_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1702_freeze_all_npcs_until_return_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_freeze_all_npcs_until_return_26',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_27_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_27_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_jump_to_height_10',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_northeast_steps_11',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_northeast_pixels_12',
                "command": 'shift_northeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_fixed_f_coord_on_14',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_east_pixels_16',
                "command": 'shift_east_pixels',
                "args": [50]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_jump_to_height_18',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_east_pixels_19',
                "command": 'shift_east_pixels',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0x8b]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_set_animation_speed_22',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_play_sound_23',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_jump_to_height_24',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_shift_east_steps_25',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_28_SUBSCRIPT_visibility_off_26',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [140]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_add_z_coord_1_step_7',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_29_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0xf2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_shift_east_steps_3',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_shift_west_steps_5',
                "command": 'shift_west_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1702_action_queue_async_30_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_unfreeze_all_npcs_31',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1702_action_queue_sync_32_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_1702_action_queue_sync_32_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1702_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1702_ret_34',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
