from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2406_jmp_if_objects_less_than_xy_steps_apart_0',
        "command": 'jmp_if_objects_less_than_xy_steps_apart',
        "args": [AreaObjects.MARIO, AreaObjects.NPC_9, 0x0c, 0x0c, 'EVENT_2406_action_queue_sync_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_2_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [200, 200]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._159_STAR_HILL_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_short_5',
        "command": 'set_short',
        "args": [0x700a, 0x00d2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_fade_out_music_8',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_9_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [23, 60]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_10',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_summon_to_current_level_at_marios_coords_11',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_12',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_13_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_14_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_15',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_16',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_17',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_18',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_19',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_20',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_21',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_22',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_stop_sound_23',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_24',
        "command": 'pause',
        "args": [68],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_25_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_26_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [80]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_27',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 394],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_29',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_30_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_short_31',
        "command": 'pause_short',
        "args": [544],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_32_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_32_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_33',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [68]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [56]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_35',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_36',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_37_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_37_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_short_39',
        "command": 'pause_short',
        "args": [464],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_40_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_40_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_40_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_40_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [16]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_41_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [67]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_41_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_42',
        "command": 'pause',
        "args": [73],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_fade_out_to_black_async_duration_43',
        "command": 'fade_out_to_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_run_star_piece_sequence_44',
        "command": 'run_star_piece_sequence',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_45_SUBSCRIPT_shift_z_down_steps_0',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_45_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [5]
            },
        ]
    },
    {
        "identifier": 'EVENT_2406_set_action_script_async_46',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_fade_in_from_black_async_47',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_48',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_49',
        "command": 'set_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_50',
        "command": 'set_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_51',
        "command": 'set_bit_7_offset',
        "args": [0x015c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_db_52',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_script_until_effect_done_53',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_run_dialog_54',
        "command": 'run_dialog',
        "args": [3442, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_55',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_57',
        "command": 'pause',
        "args": [52],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_play_sound_58',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_59',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_db_60',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_script_until_effect_done_61',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_62',
        "command": 'clear_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_63',
        "command": 'clear_bit_7_offset',
        "args": [0x015a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_64',
        "command": 'clear_bit_7_offset',
        "args": [0x015c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_65',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_pause_66',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_67',
        "command": 'play_music_default_volume',
        "args": [Music._34_STAR_HILL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_unfreeze_camera_68',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2406_ret_69',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
