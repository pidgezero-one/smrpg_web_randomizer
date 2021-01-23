from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1396_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 3, 'EVENT_1396_open_location_15']
    },
    {
        "identifier": 'EVENT_1396_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 2, 'EVENT_1396_action_queue_sync_17']
    },
    {
        "identifier": 'EVENT_1396_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7053, 0, 'EVENT_1396_open_location_15']
    },
    {
        "identifier": 'EVENT_1396_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 7, 'EVENT_1396_open_location_15']
    },
    {
        "identifier": 'EVENT_1396_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_5_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_6',
        "command": 'run_dialog',
        "args": [2757, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_7_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 32]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_7_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [7, 38]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_8_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_9',
        "command": 'run_dialog',
        "args": [2758, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_reset_coords_10',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1396_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1396_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 146]
    },
    {
        "identifier": 'EVENT_1396_set_bit_13',
        "command": 'set_bit',
        "args": [0x7052, 7]
    },
    {
        "identifier": 'EVENT_1396_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1396_open_location_15',
        "command": 'open_location',
        "args": [Locations._008_MARIOS_PAD, [6, 7]]
    },
    {
        "identifier": 'EVENT_1396_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1396_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_face_southeast_12',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_stop_sound_18',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_reset_properties_19',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_17_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_shirt_to_xy_coords_5',
                "command": 'shirt_to_xy_coords',
                "args": [11, 50]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_18_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_19_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_pause_20',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1396_set_21',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1396_dec_current_HP_7000_22',
        "command": 'dec_current_HP_7000',
        "args": [PlayableCharacters.MARIO]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_23',
        "command": 'run_dialog',
        "args": [2765, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_set_24',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_1396_set_25',
        "command": 'set',
        "args": [0x7000, 2752]
    },
    {
        "identifier": 'EVENT_1396_run_event_as_subroutine_26',
        "command": 'run_event_as_subroutine',
        "args": [3827]
    },
    {
        "identifier": 'EVENT_1396_pause_27',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_28',
        "command": 'run_dialog',
        "args": [2766, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_jmp_if_dialog_option_b_29',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1396_run_dialog_43']
    },
    {
        "identifier": 'EVENT_1396_run_dialog_30',
        "command": 'run_dialog',
        "args": [2750, AreaObjects.NPC_1, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_unsync_dialog_31',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1396_set_7000_to_tapped_button_32',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1396_pause_33',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1396_mem_7000_and_const_34',
        "command": 'mem_7000_and_const',
        "args": [0x0010]
    },
    {
        "identifier": 'EVENT_1396_jmp_if_7000_equals_short_35',
        "command": 'jmp_if_7000_equals_short',
        "args": [16, 'EVENT_1396_close_dialog_37']
    },
    {
        "identifier": 'EVENT_1396_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1396_set_7000_to_tapped_button_32']
    },
    {
        "identifier": 'EVENT_1396_close_dialog_37',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1396_run_menu_tutorial_38',
        "command": 'run_menu_tutorial',
        "args": [Tutorials._01_HOW_TO_USE_ITEMS]
    },
    {
        "identifier": 'EVENT_1396_fade_in_from_black_async_39',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1396_pause_40',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_41',
        "command": 'run_dialog',
        "args": [2942, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_1396_pause_44']
    },
    {
        "identifier": 'EVENT_1396_run_dialog_43',
        "command": 'run_dialog',
        "args": [2941, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_44',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_45_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_45_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_pause_46',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_47',
        "command": 'run_dialog',
        "args": [2943, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_48',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 50]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [27]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 4]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_jump_to_height_9',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 4]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_jump_to_height_12',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_49_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1396_action_queue_sync_50_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_51_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_51_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_51_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_51_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_51_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [18]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_52',
        "command": 'run_dialog',
        "args": [2944, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_jmp_if_dialog_option_b_53',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1396_pause_63']
    },
    {
        "identifier": 'EVENT_1396_run_dialog_54',
        "command": 'run_dialog',
        "args": [2945, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_55',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1396_start_battle_56',
        "command": 'start_battle',
        "args": [0x00cd, 9]
    },
    {
        "identifier": 'EVENT_1396_remove_from_current_level_57',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1396_fade_in_from_black_async_58',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1396_pause_59',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_60',
        "command": 'run_dialog',
        "args": [2947, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_61',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1396_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_1396_action_queue_async_72']
    },
    {
        "identifier": 'EVENT_1396_pause_63',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_64_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_64_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_64_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_64_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_65',
        "command": 'run_dialog',
        "args": [2946, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_66',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_67_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_pause_68',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_69_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_69_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_pause_70',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_71',
        "command": 'run_dialog',
        "args": [2949, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_72_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_pause_73',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_74',
        "command": 'run_dialog',
        "args": [2943, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_pause_75',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_76_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_76_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_run_dialog_77',
        "command": 'run_dialog',
        "args": [2948, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1396_set_78',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_1396_set_79',
        "command": 'set',
        "args": [0x7000, 2753]
    },
    {
        "identifier": 'EVENT_1396_run_event_as_subroutine_80',
        "command": 'run_event_as_subroutine',
        "args": [3827]
    },
    {
        "identifier": 'EVENT_1396_put_inventory_81',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1396_put_inventory_82',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1396_pause_83',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1396_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1396_action_queue_async_84_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1396_remove_from_current_level_85',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1396_set_bit_86',
        "command": 'set_bit',
        "args": [0x7053, 3]
    },
    {
        "identifier": 'EVENT_1396_set_bit_87',
        "command": 'set_bit',
        "args": [0x7065, 3]
    },
    {
        "identifier": 'EVENT_1396_set_bit_88',
        "command": 'set_bit',
        "args": [0x7065, 2]
    },
    {
        "identifier": 'EVENT_1396_set_bit_89',
        "command": 'set_bit',
        "args": [0x706d, 2]
    },
    {
        "identifier": 'EVENT_1396_ret_90',
        "command": 'ret'
    }
]
