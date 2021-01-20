from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3200_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_3_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_7',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_11',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_shift_z_down_pixels_14',
                "command": 'shift_z_down_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_sequence_playback_on_17',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_db_18',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_db_19',
                "command": 'db',
                "args": [0x25, 0x00, 0x10, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_floating_on_20',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_bpl_26_27_28_22',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_floating_off_23',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_solidity_bits_24',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_26',
                "command": 'walk_to_xy_coords',
                "args": [7, 49]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_start_embedded_action_script_async_6',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_west_pixels_6',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_east_pixels_8',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_shift_north_pixels_9',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_end_loop_10',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_6_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_start_embedded_action_script_async_7',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_clear_bit_2',
                "command": 'clear_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_7_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3200_action_queue_async_8_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_bit_5',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_jump_to_height_silent_13',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_floating_on_14',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_walk_1_step_south_15',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_vram_priority_16',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_8_SUBSCRIPT_set_solidity_bits_17',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 4, 'EVENT_3200_pause_55'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_10',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._012_DIZZINESS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_12',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 8, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_13',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 0, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_14',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_15',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 8, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_16',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 0, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_17',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_20',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 15, 71],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_21',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_fade_out_to_black_async_duration_22',
        "command": 'fade_out_to_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pixelate_layers_23',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2], 0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_summon_to_current_level_24',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_25_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_summon_to_current_level_26',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_summon_to_current_level_27',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_summon_to_current_level_28',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_29',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_fade_in_from_black_async_duration_30',
        "command": 'fade_in_from_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_31_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_32_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_32_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_33_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_33_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_34_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_34_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_run_dialog_35',
        "command": 'run_dialog',
        "args": [1640, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_36_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [56]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_37_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_37_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [48]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_38_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [72]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_run_dialog_39',
        "command": 'run_dialog',
        "args": [1641, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_start_embedded_action_script_async_40',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_start_embedded_action_script_async_40_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_walk_1_step_south_7',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x80, 0x04, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_db_15',
                "command": 'db',
                "args": [0x25, 0x80, 0x04, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_bpl_26_27_28_18',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_sequence_looping_off_19',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_jump_to_height_20',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_walk_1_step_southeast_21',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_face_northwest_23',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_face_northeast_25',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_set_vram_priority_26',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_sequence_looping_on_27',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_sequence_playback_on_28',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_set_animation_speed_29',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_jump_to_height_30',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_play_sound_32',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_walk_to_xy_coords_33',
                "command": 'walk_to_xy_coords',
                "args": [10, 49]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_41_SUBSCRIPT_visibility_off_34',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [210]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [10, 49]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_42_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [10, 49]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_43_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [190]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_walk_to_xy_coords_7',
                "command": 'walk_to_xy_coords',
                "args": [10, 49]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_44_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 6]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=3, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_45_SUBSCRIPT_jump_to_height_silent_15',
                "command": 'jump_to_height_silent',
                "args": [72]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_46_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_sync_46_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_run_dialog_47',
        "command": 'run_dialog',
        "args": [1642, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_store_coin_amount_7000_48',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_dec_coins_49',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x70b6, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_mem_7000_shift_left_51',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_set_short_mem_52',
        "command": 'set_short_mem',
        "args": [0x70b7, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_set_bit_53',
        "command": 'set_bit',
        "args": [0x7056, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_ret_54',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_pause_55',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3200_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 4]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_floating_on_8',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3200_action_queue_async_56_SUBSCRIPT_clear_bit_10',
                "command": 'clear_bit',
                "args": [0x7043, 1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3200_ret_57',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
