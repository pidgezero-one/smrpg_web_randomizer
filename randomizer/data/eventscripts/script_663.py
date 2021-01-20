from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_663_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70af],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_663_adjust_music_tempo_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_6',
        "command": 'set',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_dec_short_mem_7',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70af],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_10',
        "command": 'run_dialog',
        "args": [2504, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_adjust_music_tempo_12',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_stop_background_event_13',
        "command": 'stop_background_event',
        "args": [timer_memory=0x701c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_stop_background_event_14',
        "command": 'stop_background_event',
        "args": [timer_memory=0x701e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_mem_compare_16',
        "command": 'mem_compare',
        "args": [0x7000, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_comparison_result_is_greater_or_equal_17',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_663_set_short_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_mem_compare_18',
        "command": 'mem_compare',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_comparison_result_is_greater_or_equal_19',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_663_set_short_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_mem_compare_20',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_comparison_result_is_greater_or_equal_21',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_663_set_short_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_22',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_663_jmp_to_event_317'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_24',
        "command": 'set_short',
        "args": [0x7024, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_663_jmp_to_event_317'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_26',
        "command": 'set_short',
        "args": [0x7024, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_663_jmp_to_event_317'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_short_28',
        "command": 'set_short',
        "args": [0x7024, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_663_jmp_to_event_317'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_30_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_30_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_30_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [21, 73, 1]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_30_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_30_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_31_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_31_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_31_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_33',
        "command": 'run_dialog',
        "args": [2505, AreaObjects.NPC_15, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_34',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [21, 73, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_35_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_36',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_37_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_37_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_37_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_37_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_38',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_39',
        "command": 'run_dialog',
        "args": [2138, AreaObjects.NPC_16, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_40',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_41',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_42_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_43',
        "command": 'run_dialog',
        "args": [2139, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_44',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [240]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_set_vram_priority_7',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_45_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_remember_last_object_47',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_48',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_50_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_50_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_50_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_50_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 254, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_remember_last_object_51',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_52',
        "command": 'run_dialog',
        "args": [2106, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_53',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_54_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_54_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_55',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_56',
        "command": 'run_dialog',
        "args": [2131, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_57',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_58',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_59_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_60',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_61_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_62',
        "command": 'run_dialog',
        "args": [2128, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_stop_sound_5',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_63_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_64',
        "command": 'run_dialog',
        "args": [2129, AreaObjects.NPC_13, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_65',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_66_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_66_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_66_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_66_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_67_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_67_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_68',
        "command": 'run_dialog',
        "args": [2130, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_69',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_70_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_70_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_71',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_72',
        "command": 'run_dialog',
        "args": [2127, AreaObjects.NPC_15, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_73',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_75',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_76',
        "command": 'run_dialog',
        "args": [2132, AreaObjects.NPC_16, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_77_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_78',
        "command": 'run_dialog',
        "args": [2133, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_79',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_80',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_81',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_82_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_83_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_84_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_85_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_85_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_85_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_86',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_87',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_88',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_var_equals_short_89',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 4, 'EVENT_663_set_bit_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_var_equals_short_90',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 3, 'EVENT_663_set_bit_128'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_var_equals_short_91',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 2, 'EVENT_663_set_bit_143'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_enter_area_92',
        "command": 'enter_area',
        "args": [Rooms._063_MARRYMORE_SCENE, RadialDirections.SOUTH, 12, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_93_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_94',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 72, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_95',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_96',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_97',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_98_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_98_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_99',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_99_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_99_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_99_SUBSCRIPT_stop_sound_2',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_99_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._108_DRUM_ROLL_END, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_99_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_100',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_101',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_apply_tile_mod_102',
        "command": 'apply_tile_mod',
        "args": [Rooms._063_MARRYMORE_SCENE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_103',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_apply_tile_mod_104',
        "command": 'apply_tile_mod',
        "args": [Rooms._063_MARRYMORE_SCENE, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_105',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_apply_tile_mod_106',
        "command": 'apply_tile_mod',
        "args": [Rooms._063_MARRYMORE_SCENE, 3, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_107',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_shift_west_steps_3',
                "command": 'shift_west_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_stop_sound_4',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._108_DRUM_ROLL_END, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_108_SUBSCRIPT_shift_west_pixels_6',
                "command": 'shift_west_pixels',
                "args": [12]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_109',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_event_as_subroutine_110',
        "command": 'run_event_as_subroutine',
        "args": [272],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_111',
        "command": 'jmp',
        "args": ['EVENT_663_circle_mask_static_156'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_bit_112',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_enter_area_113',
        "command": 'enter_area',
        "args": [Rooms._063_MARRYMORE_SCENE, RadialDirections.SOUTH, 12, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_114_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_115',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_115_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_115_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_116',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 48, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_117',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_118',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_119',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_shift_east_steps_2',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_stop_sound_3',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._108_DRUM_ROLL_END, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_120_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_121_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_121_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_121_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_122',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_stop_music_123',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_124',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_125',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_event_as_subroutine_126',
        "command": 'run_event_as_subroutine',
        "args": [272],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_127',
        "command": 'jmp',
        "args": ['EVENT_663_circle_mask_static_156'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_bit_128',
        "command": 'set_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_enter_area_129',
        "command": 'enter_area',
        "args": [Rooms._063_MARRYMORE_SCENE, RadialDirections.SOUTH, 12, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_130',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_130_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_apply_tile_mod_131',
        "command": 'apply_tile_mod',
        "args": [Rooms._063_MARRYMORE_SCENE, 2, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_132',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_133',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 48, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_134',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_135',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_136_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_136_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_stop_sound_3',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._108_DRUM_ROLL_END, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_137_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_138_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_138_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_138_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_138_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [10]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_139',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_140',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_event_as_subroutine_141',
        "command": 'run_event_as_subroutine',
        "args": [272],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_142',
        "command": 'jmp',
        "args": ['EVENT_663_circle_mask_static_156'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_bit_143',
        "command": 'set_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_enter_area_144',
        "command": 'enter_area',
        "args": [Rooms._063_MARRYMORE_SCENE, RadialDirections.SOUTH, 12, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_145',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_145_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_146',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 48, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_147',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_sound_148',
        "command": 'play_sound',
        "args": [Sounds._107_DRUM_ROLL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_149',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_149_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_149_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_stop_sound_3',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._108_DRUM_ROLL_END, 6]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_150_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_151_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_151_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_151_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_151_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_151_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_152',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_153',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_event_as_subroutine_154',
        "command": 'run_event_as_subroutine',
        "args": [272],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_155',
        "command": 'jmp',
        "args": ['EVENT_663_circle_mask_static_156'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_circle_mask_static_156',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_157',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_enter_area_158',
        "command": 'enter_area',
        "args": [Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, RadialDirections.SOUTHWEST, 21, 71, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_play_music_default_volume_159',
        "command": 'play_music_default_volume',
        "args": [Music._39_MARRYMORE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_160',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_160_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_161',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_161_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [23, 117, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_162_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [23, 117, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_163_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [23, 117, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_jmp_if_bit_set_164',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_663_palette_set_201'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_bit_set_165',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_663_action_queue_sync_241'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_jmp_if_bit_set_166',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_663_action_queue_sync_278'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_167',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_167_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_168',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_168_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_168_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 68, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_168_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_168_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_168_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_169',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_169_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 70, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_169_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_169_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [12, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_169_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_170',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_170_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_170_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [22, 72, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_170_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_170_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_fade_in_from_black_sync_duration_171',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_172',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_173',
        "command": 'run_dialog',
        "args": [2134, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_174',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_175',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_176',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_177',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_177_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_177_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_177_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_177_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_178',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_178_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_178_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_178_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_178_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_179',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_179_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_180',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_180_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_180_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_181',
        "command": 'run_dialog',
        "args": [2135, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_182',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_183',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_183_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_184_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_185',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_face_west_4',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_185_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_186',
        "command": 'run_dialog',
        "args": [2136, AreaObjects.NPC_16, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_187',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_188',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_188_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_189',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_189_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_190',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_190_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_191',
        "command": 'run_dialog',
        "args": [2137, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_192',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_193',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_193_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_193_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_193_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_194',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_195',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_195_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_196',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_197',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_197_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_198',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_199',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_199_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_199_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_199_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_199_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_jmp_to_event_200',
        "command": 'jmp_to_event',
        "args": [668],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_palette_set_201',
        "command": 'palette_set',
        "args": [142, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_202',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_202_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [22, 72, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_202_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_202_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_202_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_203_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [22, 73, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_203_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_204',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_204_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 70, 2, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_205',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_205_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 71, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_205_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_205_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_205_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_fade_in_from_black_sync_duration_206',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_207',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_208',
        "command": 'run_dialog',
        "args": [2134, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_209',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_210',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_210_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_210_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_210_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_210_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_210_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_211',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_212',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_212_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_213',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southeast_15',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_17',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_21',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southeast_23',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_25',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_northwest_27',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_29',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_face_southwest_31',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_213_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [60]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_214',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_214_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_214_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_214_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_214_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_214_SUBSCRIPT_stop_sound_4',
                "command": 'stop_sound',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_215',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_215_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_palette_set_216',
        "command": 'palette_set',
        "args": [84, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_217',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_217_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_217_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_217_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_218',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_218_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_218_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_219',
        "command": 'run_dialog',
        "args": [2135, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_220',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_221',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_222',
        "command": 'run_dialog',
        "args": [2136, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_223',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_224',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_224_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_225',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_225_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_225_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_225_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_225_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_225_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_226',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_226_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_226_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_226_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_226_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_226_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_227',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_227_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_227_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_227_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_227_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_227_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_228',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_229',
        "command": 'run_dialog',
        "args": [2137, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_230',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_231',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_232',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_233',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_233_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_233_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_233_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [20, 116, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_234',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_234_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_234_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_remember_last_object_235',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_236',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_237',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_237_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [20, 116, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_238',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_239',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_239_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_jmp_to_event_240',
        "command": 'jmp_to_event',
        "args": [668],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_241',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_241_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 70, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_241_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_242',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_242_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_242_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 68, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_242_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_242_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_242_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_243',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_243_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 71, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_243_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_243_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_244',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_244_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [22, 73, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_244_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_244_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_fade_in_from_black_sync_duration_245',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_246',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_247',
        "command": 'run_dialog',
        "args": [2151, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_248',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_249',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_250',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_251',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_251_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_252',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_252_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_252_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_253',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_253_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_254',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_254_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_254_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_255',
        "command": 'run_dialog',
        "args": [2135, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_256',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_257',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_257_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_257_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_258',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_258_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_259',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_face_west_4',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_259_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_260',
        "command": 'run_dialog',
        "args": [2136, AreaObjects.NPC_16, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_261',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_262',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_262_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_263',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_263_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_264',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_264_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_265',
        "command": 'run_dialog',
        "args": [2137, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_266',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_267',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_268',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_269',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_269_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_269_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_269_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_270',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_271',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_271_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_271_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_271_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_272',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_273',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_273_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_274',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_275',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_275_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_275_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_276',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_276_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_jmp_to_event_277',
        "command": 'jmp_to_event',
        "args": [668],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_278',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_278_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 70, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_278_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_279',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_279_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_279_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 68, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_279_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_279_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_279_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_280',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_280_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [22, 72, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_280_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_280_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_280_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_281',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_281_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [21, 71, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_281_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_281_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_281_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_fade_in_from_black_sync_duration_282',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_script_until_effect_done_283',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_284',
        "command": 'run_dialog',
        "args": [2152, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_285',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_set_action_script_async_286',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_287',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_288',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_288_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_288_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_288_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_288_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_289',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_289_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_290',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_290_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_290_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_291',
        "command": 'run_dialog',
        "args": [2135, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_292',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_293',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_293_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_294',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_294_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_295',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_face_west_4',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_295_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_296',
        "command": 'run_dialog',
        "args": [2136, AreaObjects.NPC_16, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_297',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_298',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_async_298_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_299',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_299_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_async_300',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_300_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_run_dialog_301',
        "command": 'run_dialog',
        "args": [2137, AreaObjects.NPC_16, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_302',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_303',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_303_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_303_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_303_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_304',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_305',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_305_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_306',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_307',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_307_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_307_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_307_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_307_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_308',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_308_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_309',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_309_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_remember_last_object_310',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_pause_311',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_sync_312',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_sync_312_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_312_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_312_SUBSCRIPT_face_east_2',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_312_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_sync_312_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_663_pause_313',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_run_dialog_314',
        "command": 'run_dialog',
        "args": [2123, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_remember_last_object_315',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_663_action_queue_async_316',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_663_action_queue_async_316_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_316_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_316_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_316_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_663_action_queue_async_316_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_663_jmp_to_event_317',
        "command": 'jmp_to_event',
        "args": [668],
        "subscript": []
    },
]
