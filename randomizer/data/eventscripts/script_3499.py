from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3499_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_set_short_1',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3499_set_short_2',
        "command": 'set_short',
        "args": [0x7034, 0x0010]
    },
    {
        "identifier": 'EVENT_3499_set_short_3',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_3499_set_4',
        "command": 'set',
        "args": [0x70b1, 0]
    },
    {
        "identifier": 'EVENT_3499_freeze_camera_5',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 67, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_3],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_7_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [18]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_10_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_11_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 715]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x6d15]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_14',
        "command": 'jmp_to_subroutine',
        "args": [0x6d30]
    },
    {
        "identifier": 'EVENT_3499_pause_15',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_16',
        "command": 'jmp_to_subroutine',
        "args": [0x6d15]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": [0x6d30]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_18',
        "command": 'jmp_to_subroutine',
        "args": [0x6d15]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_19',
        "command": 'jmp_to_subroutine',
        "args": [0x6d30]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_20_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_20_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_21',
        "command": 'jmp_to_subroutine',
        "args": [0x6d15]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_22',
        "command": 'jmp_to_subroutine',
        "args": [0x6d30]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_23_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_23_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_23_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_24',
        "command": 'jmp_to_subroutine',
        "args": [0x6d15]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_25_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_26_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_set_27',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_28',
        "command": 'jmp_to_subroutine',
        "args": [0x6d30]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 707]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 707]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 707]
    },
    {
        "identifier": 'EVENT_3499_pause_32',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3499_freeze_all_npcs_until_return_33',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_3499_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3499_pause_67']
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_35',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 1]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_36',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 2]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_37',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 3]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_38',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 4]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_39',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 5]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_40',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 6]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_41',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 7]
    },
    {
        "identifier": 'EVENT_3499_pause_42',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 65, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_43_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [107]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_shift_southwest_pixels_11',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_jump_to_height_14',
                "command": 'jump_to_height',
                "args": [107]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_44_SUBSCRIPT_end_loop_16',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": [0x6d49]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_46_SUBSCRIPT_shift_northwest_pixels_15',
                "command": 'shift_northwest_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._050_WATER_DROPLET, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_47_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [84]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_48_SUBSCRIPT_transfer_to_xyzf_13',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_49_SUBSCRIPT_shift_xy_steps_1',
                "command": 'shift_xy_steps',
                "args": [3, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_50_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_50_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_50_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_jmp_to_subroutine_51',
        "command": 'jmp_to_subroutine',
        "args": [0x6d49]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [17]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_52_SUBSCRIPT_transfer_to_xyzf_9',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._050_WATER_DROPLET, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_53_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_54_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [32]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_async_55',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 716]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_56_SUBSCRIPT_shift_xy_steps_1',
                "command": 'shift_xy_steps',
                "args": [254, 252]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_57_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_57_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_57_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_fade_out_music_to_volume_58',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_59_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_59_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_59_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_60',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 97, 1]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_61',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 98, 2]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_62',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 99, 3]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_63',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 100, 4]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_64',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 101, 5]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_65',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 102, 6]
    },
    {
        "identifier": 'EVENT_3499_palette_set_morphs_66',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 103, 7]
    },
    {
        "identifier": 'EVENT_3499_pause_67',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3499_unfreeze_all_npcs_68',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_3499_run_background_event_69',
        "command": 'run_background_event',
        "args": [3500, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3499_run_background_event_70',
        "command": 'run_background_event',
        "args": [3503, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_3499_stop_sound_71',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_72',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_73',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_74',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_75',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_76',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_77',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_78',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_79',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_80',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_81',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_82',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_83',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_84',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_85',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_86',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_87',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_88',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_89',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_90',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_91',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_92',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_93',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_94',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_95',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_96',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_97',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_98',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_99',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_100',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_101',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_102',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_103',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_104',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_105',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_106',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_107',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_108',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_109',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_110',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_111',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_112',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_113',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_114',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_115',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_116',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_117',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_118',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_119',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_120',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_121',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_122',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_stop_sound_123',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_124',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_1, 704]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_125',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 655]
    },
    {
        "identifier": 'EVENT_3499_set_action_script_sync_126',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_3, 705]
    },
    {
        "identifier": 'EVENT_3499_play_music_default_volume_127',
        "command": 'play_music_default_volume',
        "args": [Music._38_BOOSTER_HILL]
    },
    {
        "identifier": 'EVENT_3499_run_event_at_return_128',
        "command": 'run_event_at_return',
        "args": [3502]
    },
    {
        "identifier": 'EVENT_3499_ret_129',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_130_SUBSCRIPT_set_object_memory_bits_6',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_131',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_131_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_131_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_131_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_131_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_ret_132',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_133_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_async_134_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_134_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_134_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_async_134_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_ret_135',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 54, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_jump_to_height_9',
                "command": 'jump_to_height',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_walk_1_step_southeast_10',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_set_700C_to_object_coord_11',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_mem_compare_12',
                "command": 'mem_compare',
                "args": [0x700c, 5888]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_136_SUBSCRIPT_jmp_if_comparison_result_is_lesser_13',
                "command": 'jmp_if_comparison_result_is_lesser',
                "args": ['EVENT_3499_action_queue_sync_136_SUBSCRIPT_jump_to_height_9']
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3499_action_queue_sync_137_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3499_action_queue_sync_137_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [112]
            }
        ]
    },
    {
        "identifier": 'EVENT_3499_ret_138',
        "command": 'ret'
    }
]
