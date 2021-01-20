from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3282_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 7, 'EVENT_3282_jmp_if_bit_set_129'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_3282_start_battle_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_2_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_party_capacity_4',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_7_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_7_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_7_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_7_SUBSCRIPT_shift_east_steps_4',
                "command": 'shift_east_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_mem_compare_8',
        "command": 'mem_compare',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_9',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_member_in_slot_11',
        "command": 'set_short_member_in_slot',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_var_not_equals_short_12',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 3, 'EVENT_3282_clear_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_bit_13',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_member_in_slot_15',
        "command": 'set_short_member_in_slot',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_var_not_equals_short_16',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 2, 'EVENT_3282_clear_bit_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_bit_17',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_member_in_slot_19',
        "command": 'set_short_member_in_slot',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_var_not_equals_short_20',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 2, 'EVENT_3282_action_queue_sync_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_shift_north_steps_4',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 0, 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_8']
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_ret_7',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_22_SUBSCRIPT_ret_9',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_23_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_24_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_25_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_26_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_27_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_27_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_27_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_28_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_28_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_28_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_29_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_run_dialog_30',
        "command": 'run_dialog',
        "args": [1776, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_object_memory_modify_bits_4',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_31_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_start_battle_32',
        "command": 'start_battle',
        "args": [0x00a6, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_current_level_33',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_current_level_34',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_current_level_35',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_37',
        "command": 'clear_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_stop_music_39',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_run_event_as_subroutine_40',
        "command": 'run_event_as_subroutine',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_bit_41',
        "command": 'set_bit',
        "args": [0x7058, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_3282_restore_all_hp_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_43_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_43_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_43_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_run_dialog_44',
        "command": 'run_dialog',
        "args": [1777, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_restore_all_hp_45',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_restore_all_fp_46',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_3282_fade_in_music_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_play_music_default_volume_48',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_49',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_db_50',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0x2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_51',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_52',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_transfer_to_object_xy_2',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_53_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_10',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_shift_z_up_pixels_12',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_54_SUBSCRIPT_set_priority_13',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [512]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_55_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_56_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_pause_action_script_57',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_party_capacity_58',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_mem_compare_59',
        "command": 'mem_compare',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_60',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_61_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_61_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_61_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_mem_compare_62',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_63',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_64_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_64_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_64_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_65_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_66',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_67',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [88]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_69_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [90]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_70_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_pause_71',
        "command": 'pause',
        "args": [165],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_play_music_default_volume_72',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_73',
        "command": 'pause',
        "args": [102],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xc8, 0x00]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_add_short_5',
                "command": 'add_short',
                "args": [0x701a, 0x0220]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_74_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_set_short_party_capacity_75',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_mem_compare_76',
        "command": 'mem_compare',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_77',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_async_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 2, 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_4']
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_mem_compare_79',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_80',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_async_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 1, 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_4']
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_pause_83',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_84_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_84_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_84_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_84_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_1]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 8, RadialDirections.NORTHEAST]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_85_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[1]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_86_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_86_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_86_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_86_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_db_87',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0c, 0x28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_88',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_89',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_90',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_91_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_91_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_91_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_pause_92',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_run_star_piece_sequence_93',
        "command": 'run_star_piece_sequence',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_94',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_current_level_95',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_level_96',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_97_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_97_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_97_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_set_short_party_capacity_98',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_mem_compare_99',
        "command": 'mem_compare',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_100',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_async_105'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_101_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_101_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_mem_compare_102',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_103',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_async_105'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_104_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_104_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_105_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_105_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_db_106',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x72, 0x00, 0x28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_fade_out_music_to_volume_107',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_fade_in_from_black_async_108',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_pause_109',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_party_capacity_110',
        "command": 'set_short_party_capacity',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_mem_compare_111',
        "command": 'mem_compare',
        "args": [0x7000, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_112',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_119'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_113',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_113_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_113_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_113_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_113_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_113_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.CHARACTER_IN_SLOT_3],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_3282_action_queue_async_114_SUBSCRIPT_reset_properties_7']
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_114_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_mem_compare_115',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_comparison_result_is_lesser_116',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3282_action_queue_sync_119'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_117_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_117_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_117_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_117_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_117_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_118_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_119_SUBSCRIPT_face_south_5',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_action_queue_async_120',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_async_120_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_120_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_120_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_async_120_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_fade_in_music_121',
        "command": 'fade_in_music',
        "args": [Music._41_SUNKEN_SHIP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_level_122',
        "command": 'remove_from_level',
        "args": [AreaObjects.MARIO, Rooms._000_DEBUG_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_level_123',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_level_124',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_remove_from_level_125',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_short_126',
        "command": 'set_short',
        "args": [0x700a, 0x00d5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_to_event_127',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_ret_128',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_if_bit_set_129',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_3282_jmp_to_event_133'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_set_action_script_sync_130',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3282_action_queue_sync_131_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [24, 110]
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_131_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_131_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3282_action_queue_sync_131_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3282_jmp_to_event_132',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3282_jmp_to_event_133',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
]
