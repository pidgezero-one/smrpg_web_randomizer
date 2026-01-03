
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3121_summon_to_current_level_at_marios_coords_0',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3121_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_walk_to_xy_coords_9',
                "command": 'walk_to_xy_coords',
                "args": [7, 38]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_fixed_f_coord_off_10',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_shift_east_steps_15',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_face_northwest_16',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_shift_north_steps_18',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_face_southwest_19',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_shift_west_steps_21',
                "command": 'shift_west_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_face_southeast_22',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_shift_south_steps_24',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_face_northeast_25',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_1_SUBSCRIPT_set_bit_28',
                "command": 'set_bit',
                "args": [0x7043, 2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_set_object_memory_bits_3',
                "command": 'set_object_memory_bits',
                "args": [0x0b, []]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [6, 37]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_2_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_fade_out_music_to_volume_3',
        "command": 'fade_out_music_to_volume',
        "args": [16, 0]
    },
    {
        "identifier": 'EVENT_3121_run_dialog_4',
        "command": 'run_dialog',
        "args": [1588, AreaObjects.NPC_2, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3121_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3121_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3121_pause_5']
    },
    {
        "identifier": 'EVENT_3121_close_dialog_7',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3121_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_sync_8_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_9',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_9_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_9_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_10_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_run_dialog_11',
        "command": 'run_dialog',
        "args": [1589, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3121_start_battle_12',
        "command": 'start_battle',
        "args": [0x00a8, 21]
    },
    {
        "identifier": 'EVENT_3121_set_bit_13',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_3121_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_3121_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_3121_run_event_as_subroutine_16',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3121_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._303_KERO_SEWERS_AREA_08_BELOMES_ROOM_AFTER_DEFEAT, RadialDirections.NORTHEAST, 6, 37, 1, []]
    },
    {
        "identifier": 'EVENT_3121_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_async_18_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 38, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3121_action_queue_async_18_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_async_18_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3121_action_queue_async_18_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_fade_in_from_black_async_19',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3121_set_bit_20',
        "command": 'set_bit',
        "args": [0x7055, 2]
    },
    {
        "identifier": 'EVENT_3121_restore_all_hp_21',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_3121_restore_all_fp_22',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_3121_pause_23',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3121_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_3121_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 56]
    },
    {
        "identifier": 'EVENT_3121_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_26_SUBSCRIPT_walk_1_step_northeast_6',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._017_OPEN_FRONT_GATE, 6]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_steps_10',
                "command": 'shift_south_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_jmp_if_bit_clear_12',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_11']
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_13',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_jmp_if_bit_clear_15',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_13']
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_shift_south_steps_16',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_action_queue_sync_27_SUBSCRIPT_set_bit_17',
                "command": 'set_bit',
                "args": [0x7043, 3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_run_dialog_28',
        "command": 'run_dialog',
        "args": [1592, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3121_set_bit_29',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_3121_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._007_GUSHING_WATER, 4]
    },
    {
        "identifier": 'EVENT_3121_run_dialog_31',
        "command": 'run_dialog',
        "args": [1593, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3121_set_bit_32',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_3121_pause_action_script_33',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3121_pause_34',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_3121_run_dialog_35',
        "command": 'run_dialog',
        "args": [1594, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3121_freeze_camera_36',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_13',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_northeast_steps_14',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_shift_northeast_steps_16',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_18',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jmp_if_bit_clear_20',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 3, 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_jump_to_height_18']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_reset_properties_21',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_face_northeast_22',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_37_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_northwest_steps_11',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_northeast_steps_15',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_jump_to_height_16',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_solidity_bits_18',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_walk_1_step_northeast_19',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_bit_20',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_clear_solidity_bits_21',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_z_down_pixels_22',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_bit_25',
                "command": 'set_bit',
                "args": [0x7043, 2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_reset_properties_26',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_jump_to_height_27',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_fixed_f_coord_on_28',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_shift_southwest_steps_29',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_38_SUBSCRIPT_set_animation_speed_31',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_jmp_if_bit_clear_2',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._009_GREEN_SWITCH, 6]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_jmp_if_bit_clear_6',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._009_GREEN_SWITCH, 6]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_39_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_pause_40',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3121_jmp_if_bit_clear_41',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3121_pause_40']
    },
    {
        "identifier": 'EVENT_3121_close_dialog_42',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3121_play_sound_43',
        "command": 'play_sound',
        "args": [Sounds._007_GUSHING_WATER, 6]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.LAYER_3],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_set_bit_2',
                "command": 'set_bit',
                "args": [0x7043, 4]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_44_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_face_south_3',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_clear_solidity_bits_5',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_jmp_if_bit_clear_7',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 4, 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_walk_1_step_southwest_12',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_walk_1_step_southwest_14',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_walk_1_step_southwest_16',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_bit_17',
                "command": 'set_bit',
                "args": [0x7043, 5]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_shift_southwest_steps_18',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_bit_19',
                "command": 'set_bit',
                "args": [0x7043, 7]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_shift_southwest_steps_20',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_bit_21',
                "command": 'set_bit',
                "args": [0x7043, 6]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_walk_1_step_southwest_22',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_solidity_bits_23',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_sequence_looping_off_25',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_45_SUBSCRIPT_reset_properties_26',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 5, 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_46_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_47',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_47_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 5, 'EVENT_3121_start_embedded_action_script_sync_F1_47_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_47_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 6, 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_sequence_playback_off_4',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3121_start_embedded_action_script_sync_F1_48_SUBSCRIPT_sequence_playback_on_7',
                "command": 'sequence_playback_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3121_pause_49',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3121_jmp_if_bit_clear_50',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_3121_pause_49']
    },
    {
        "identifier": 'EVENT_3121_fade_out_sound_to_volume_51',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_3121_fade_out_to_black_async_duration_52',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3121_unfreeze_camera_53',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3121_remove_from_current_level_54',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_3121_set_bit_55',
        "command": 'set_bit',
        "args": [0x704d, 6]
    },
    {
        "identifier": 'EVENT_3121_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7096, 5]
    },
    {
        "identifier": 'EVENT_3121_enter_area_57',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 9, 108, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3121_ret_58',
        "command": 'ret'
    }
]
