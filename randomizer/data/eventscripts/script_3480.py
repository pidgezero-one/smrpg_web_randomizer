from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3480_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3480_fade_out_music_to_volume_1',
        "command": 'fade_out_music_to_volume',
        "args": [0, 8]
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_2',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_3480_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4]
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_4',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 127]
    },
    {
        "identifier": 'EVENT_3480_set_5',
        "command": 'set',
        "args": [0x70a9, 32]
    },
    {
        "identifier": 'EVENT_3480_set_short_6',
        "command": 'set_short',
        "args": [0x7016, 0x1180]
    },
    {
        "identifier": 'EVENT_3480_set_short_7',
        "command": 'set_short',
        "args": [0x7018, 0x0100]
    },
    {
        "identifier": 'EVENT_3480_set_short_8',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'EVENT_3480_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x99]
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_add_short_11',
        "command": 'add_short',
        "args": [0x7016, 0x0080]
    },
    {
        "identifier": 'EVENT_3480_add_short_12',
        "command": 'add_short',
        "args": [0x7018, 0x0040]
    },
    {
        "identifier": 'EVENT_3480_add_13',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_3480_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3480_set_short_15',
        "command": 'set_short',
        "args": [0x7016, 0x1200]
    },
    {
        "identifier": 'EVENT_3480_set_short_16',
        "command": 'set_short',
        "args": [0x7018, 0x0200]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_17_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x99]
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_fade_in_from_black_sync_duration_18',
        "command": 'fade_in_from_black_sync_duration',
        "args": [80]
    },
    {
        "identifier": 'EVENT_3480_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 5, 'EVENT_3480_action_queue_async_22']
    },
    {
        "identifier": 'EVENT_3480_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 6, 'EVENT_3480_action_queue_async_22']
    },
    {
        "identifier": 'EVENT_3480_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [148]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [6, 73]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_shift_north_steps_5',
                "command": 'shift_north_steps',
                "args": [27]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_21_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_walk_1_step_north_3',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_walk_1_step_north_5',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_shift_north_steps_7',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_shift_north_steps_9',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_shift_north_steps_11',
                "command": 'shift_north_steps',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_shift_north_steps_13',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_shift_north_steps_15',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_walk_1_step_north_17',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_walk_1_step_north_19',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_22_SUBSCRIPT_set_solidity_bits_21',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_fade_out_music_to_volume_23',
        "command": 'fade_out_music_to_volume',
        "args": [1, 56]
    },
    {
        "identifier": 'EVENT_3480_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 5, 'EVENT_3480_action_queue_async_30']
    },
    {
        "identifier": 'EVENT_3480_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 6, 'EVENT_3480_action_queue_async_28']
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [9, 2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_shift_south_pixels_10',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_shift_south_steps_12',
                "command": 'shift_south_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_26_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3480_action_queue_sync_31']
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x00, 0x02, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_shift_southwest_steps_14',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_shift_south_steps_16',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_bpl_26_27_28_17',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_28_SUBSCRIPT_fixed_f_coord_off_18',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_3480_priority_set_60']
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 8]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_shift_south_steps_10',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x70, 0x02, 0xf5, 0xff]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_shift_northeast_steps_14',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_walk_1_step_north_15',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_30_SUBSCRIPT_bpl_26_27_28_16',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_1]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3480_action_queue_sync_31_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_32',
        "command": 'fade_out_sound_to_volume',
        "args": [4, 0]
    },
    {
        "identifier": 'EVENT_3480_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_3480_priority_set_60']
    },
    {
        "identifier": 'EVENT_3480_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_35',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 1]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_36',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 2]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_37',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 3]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_38',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 4]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_39',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 5]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_40',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 6]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_41',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 7]
    },
    {
        "identifier": 'EVENT_3480_pause_42',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3480_priority_set_43',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_1, _0x81Flags.BACKGROUND, _0x81Flags.HALF_INTENSITY]]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_44_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_stop_sound_45',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_46',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 127]
    },
    {
        "identifier": 'EVENT_3480_play_sound_47',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3480_jmp_if_dialog_option_b_48',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3480_run_dialog_duration_54']
    },
    {
        "identifier": 'EVENT_3480_run_dialog_49',
        "command": 'run_dialog',
        "args": [1084, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_shift_west_pixels_9',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_50_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_run_dialog_duration_51',
        "command": 'run_dialog_duration',
        "args": [1085, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 6]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_end_loop_7',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_shift_south_pixels_9',
                "command": 'shift_south_pixels',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_52_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_run_dialog_duration_53',
        "command": 'run_dialog_duration',
        "args": [1073, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3480_run_dialog_duration_54',
        "command": 'run_dialog_duration',
        "args": [1074, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3480_play_sound_55',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_56_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_56_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_56_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_57',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_3480_play_sound_58',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4]
    },
    {
        "identifier": 'EVENT_3480_fade_out_sound_to_volume_59',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 127]
    },
    {
        "identifier": 'EVENT_3480_priority_set_60',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_3, _0x81Flags.BACKGROUND, _0x81Flags.HALF_INTENSITY]]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_61',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 57, 1]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_62',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 58, 2]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_63',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 59, 3]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_64',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 60, 4]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_65',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 61, 5]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_66',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 62, 6]
    },
    {
        "identifier": 'EVENT_3480_palette_set_morphs_67',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 63, 7]
    },
    {
        "identifier": 'EVENT_3480_pause_68',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3480_set_action_script_sync_69',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 466]
    },
    {
        "identifier": 'EVENT_3480_jmp_to_subroutine_70',
        "command": 'jmp_to_subroutine',
        "args": [0x6247]
    },
    {
        "identifier": 'EVENT_3480_run_event_at_return_71',
        "command": 'run_event_at_return',
        "args": [3489]
    },
    {
        "identifier": 'EVENT_3480_ret_72',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3480_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3480_action_queue_async_73_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x97, 0x00]
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_73_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_73_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_73_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3480_action_queue_async_73_SUBSCRIPT_set_object_memory_bits_4',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3480_ret_74',
        "command": 'ret'
    }
]
