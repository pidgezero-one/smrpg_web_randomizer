from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3332_remove_from_current_level_0',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._357_VOLCANO_POSTCD_AREA_01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_bit_3',
        "command": 'set_bit',
        "args": [0x707e, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_bit_4',
        "command": 'set_bit',
        "args": [0x707e, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_bit_5',
        "command": 'set_bit',
        "args": [0x707e, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._388_VOLCANO_POSTCD_AREA_02],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x707e, 1, 'EVENT_3332_jmp_if_bit_clear_154'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_stop_music_14',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_music_default_volume_15',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_16_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_17_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [18, 102]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_17_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_db_19',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x19, 0x08, 0xff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_20',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_22_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_22_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_22_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_22_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_22_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [682]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_23_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_24_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_pause_action_script_25',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_28',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_30_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [248]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_pause_31',
        "command": 'pause',
        "args": [77],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_music_default_volume_32',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_embedded_action_script_async_33',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_33_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [90]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_pause_34',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_embedded_action_script_async_35',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_set_bit_3',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_4',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.DUMMY_0X07, 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_jump_to_height_silent_5']
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3332_start_embedded_action_script_async_35_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_36_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_36_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_face_west_13',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_37_SUBSCRIPT_set_bit_21',
                "command": 'set_bit',
                "args": [0x7043, 2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_pause_38',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_clear_39',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3332_pause_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_stop_music_40',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_41',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_42',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_43',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_clear_44',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3332_pause_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_db_45',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x32, 0x08, 0xff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_46_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_47_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_play_music_default_volume_48',
        "command": 'play_music_default_volume',
        "args": [Music._15_HERES_SOME_WEAPONS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_bit_49',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_50_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_51',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._040_AXEM_RED, AreaObjects.NPC_2, 'EVENT_3332_pause_52'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_52',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_53',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_54',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_55',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_loop_n_times_56',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_screen_flashes_with_colour_57',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.RED],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_58',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_end_loop_59',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_60',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_62',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_dialog_63',
        "command": 'run_dialog',
        "args": [1808, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_64_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_64_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_65',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_3, 'EVENT_3332_pause_66'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_66',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_67',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_68',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_69',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._044_AXEM_GREEN, AreaObjects.NPC_3, 'EVENT_3332_pause_70'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_70',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_71',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_72',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_73',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_loop_n_times_74',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_screen_flashes_with_colour_75',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.GREEN],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_76',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_end_loop_77',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_78',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_80',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_dialog_81',
        "command": 'run_dialog',
        "args": [1809, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_82_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_83',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_4, 'EVENT_3332_pause_84'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_84',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_85',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_86',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_87',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._043_AXEM_YELLOW, AreaObjects.NPC_4, 'EVENT_3332_pause_88'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_88',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_89',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_90',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_91',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_loop_n_times_92',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_screen_flashes_with_colour_93',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.YELLOW],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_94',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_end_loop_95',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_96',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_clear_bit_97',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_98',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_dialog_99',
        "command": 'run_dialog',
        "args": [1810, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_100',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_100_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_101',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_5, 'EVENT_3332_pause_102'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_102',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_103',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_104',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_105',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._042_AXEM_PINK, AreaObjects.NPC_5, 'EVENT_3332_pause_106'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_106',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_107',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_108',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_109',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_loop_n_times_110',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_screen_flashes_with_colour_111',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.PINK],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_112',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_end_loop_113',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_114',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_clear_bit_115',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_116',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_dialog_117',
        "command": 'run_dialog',
        "args": [1811, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_118_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_118_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_119',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_6, 'EVENT_3332_pause_120'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_120',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_121',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_122',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_create_packet_at_object_coords_jmp_if_null_123',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._041_AXEM_BLACK, AreaObjects.NPC_6, 'EVENT_3332_pause_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_124',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_125',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_126',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_127',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_start_loop_n_times_128',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_screen_flashes_with_colour_129',
        "command": 'screen_flashes_with_colour',
        "args": [Colours.WHITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_130',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_end_loop_131',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_132',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_clear_bit_133',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_summon_to_current_level_134',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_run_dialog_135',
        "command": 'run_dialog',
        "args": [1812, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_136_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_136_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_play_sound_137',
        "command": 'play_sound',
        "args": [Sounds._121_AXEM_RANGER_TELEPORT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_138',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_139',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_140',
        "command": 'play_sound',
        "args": [Sounds._121_AXEM_RANGER_TELEPORT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_141',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_142',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_143',
        "command": 'play_sound',
        "args": [Sounds._121_AXEM_RANGER_TELEPORT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_144',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_145',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_sound_146',
        "command": 'play_sound',
        "args": [Sounds._121_AXEM_RANGER_TELEPORT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_pause_147',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_148',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_149',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_149_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_149_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_149_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_149_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_sync_150_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_150_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_150_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_2',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_1, 'EVENT_3332_action_queue_sync_150_SUBSCRIPT_visibility_off_3']
            },
            {
                "identifier": 'EVENT_3332_action_queue_sync_150_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_action_queue_async_151',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3332_action_queue_async_151_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_151_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_151_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_2',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._045_AXEM_RED_TELEPORT_SFX, AreaObjects.NPC_2, 'EVENT_3332_action_queue_async_151_SUBSCRIPT_visibility_off_3']
            },
            {
                "identifier": 'EVENT_3332_action_queue_async_151_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3332_remove_from_current_level_152',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_clear_153',
        "command": 'jmp_if_bit_clear',
        "args": [0x707e, 1, 'EVENT_3332_set_bit_157'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_clear_154',
        "command": 'jmp_if_bit_clear',
        "args": [0x707e, 2, 'EVENT_3331_play_music_default_volume_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_jmp_if_bit_set_155',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_3332_set_bit_157'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_play_music_default_volume_156',
        "command": 'play_music_default_volume',
        "args": [Music._63_AXEM_RANGERS_DROP_IN],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_set_bit_157',
        "command": 'set_bit',
        "args": [0x707e, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3332_ret_158',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
