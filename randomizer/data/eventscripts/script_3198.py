from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3198_pause_script_if_menu_open_0',
        "command": 'pause_script_if_menu_open',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_resume_action_script_3',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_resume_action_script_4',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._048_MINECART_START, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_transfer_to_object_xy_1',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MEM_70A8]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_shift_xy_pixels_2',
                "command": 'shift_xy_pixels',
                "args": [240, 8]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [2, 124]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_6_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, RadialDirections.SOUTHWEST, 20, 25, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [20, 26]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_set_bit_4',
                "command": 'set_bit',
                "args": [0x7043, 2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_jmp_if_mario_in_air_9',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_8']
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_face_southeast_15',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_11_SUBSCRIPT_set_solidity_bits_16',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 6]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_end_loop_7',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_12_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [21, 24]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_shift_east_pixels_8',
                "command": 'shift_east_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_end_loop_9',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_walk_1_step_northeast_11',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_set_solidity_bits_12',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_sequence_looping_off_15',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_13_SUBSCRIPT_sequence_playback_off_16',
                "command": 'sequence_playback_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 6, 'EVENT_3198_action_queue_async_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_transfer_to_object_xy_1',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_0]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_shift_south_steps_6',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_10',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_object_memory_clear_bit_17',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_set_solidity_bits_18',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_summon_to_level_19',
                "command": 'summon_to_level',
                "args": [AreaObjects.NPC_2, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM]
            },
            {
                "identifier": 'EVENT_3198_action_queue_sync_15_SUBSCRIPT_ret_20',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_shirt_to_xy_coords_2',
                "command": 'shirt_to_xy_coords',
                "args": [21, 24]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_sequence_playback_on_4',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_shift_west_pixels_11',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_shift_east_pixels_12',
                "command": 'shift_east_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_jump_to_height_14',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_sequence_looping_on_15',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_play_sound_18',
                "command": 'play_sound',
                "args": [Sounds._079_YELP_IN_DISTANCE, 4]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_bounce_to_xy_with_height_19',
                "command": 'bounce_to_xy_with_height',
                "args": [21, 28, 0]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_play_sound_22',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 4]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_reset_properties_23',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_sequence_looping_on_24',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_jump_to_height_25',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_jump_to_height_27',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_play_sound_29',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_walk_to_xy_coords_30',
                "command": 'walk_to_xy_coords',
                "args": [19, 32]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_visibility_off_31',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_object_memory_set_bit_32',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3198_action_queue_async_16_SUBSCRIPT_db_33',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3198_summon_to_level_17',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3198_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
